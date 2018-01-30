#!/usr/bin/env python3
# coding=utf-8
import io
import os
import subprocess
import json
import configparser
from pathlib import Path

from .libs.RegistrationAPI.KKTIX import KKTIX
from .libs.RegistrationAPI.Meetup import Meetup

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


class EventParsing():
    def get_mydir(self):
        cmd = "echo $HOME"
        output = subprocess.check_output(cmd, shell=True)
        myhome = str(output.splitlines()).split("'")[1]
        my_dir = Path(myhome + "/.config/TGmeetup")
        if(my_dir.is_dir()):
            return str(my_dir)
        else:
            return None

    def wd_event_file(self, org_event, org):
        if org_event is None:
            try:
                os.remove(org[0].replace("package.json", "events.json"))
            except BaseException:
                pass
        else:
            event_file = org[0].replace("package.json", "events.json")
            with io.open(event_file, 'w', encoding='utf8') as outfile:
                str_ = json.dumps(org_event,
                                  indent=2, sort_keys=True,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))

    def add_kktix_event(self, kktix_orgs):
        kktix_api = KKTIX()
        for org in kktix_orgs:
            org_event = kktix_api.get_meetup_info(org[0], org[2])
            self.wd_event_file(org_event, org)

    def add_meetup_event(self, meetup_groups):
        mydir = self.get_mydir()
        if mydir is None:
            print("Please run the steps as the following: \n \
                  1. config API.cfg. \n 2. run 'sh install.sh'")
            pass
        config = configparser.ConfigParser()
        config.read(mydir + '/API.cfg')
        meetup_api = Meetup(
            config['MEETUP_API']['API_URL'],
            config['MEETUP_API']['API_KEY'],
            config['MEETUP_API']['client_secret'],
            config['MEETUP_API']['refresh_token'])
        access_token = meetup_api.refresh_access_token()
        for org in meetup_groups:
            org_event = meetup_api.get_meetup_info(access_token, org[2])
            self.wd_event_file(org_event, org)
