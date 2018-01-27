#!/usr/bin/env python3
# coding=utf-8

import os
import json
import argparse
import configparser
import subprocess
from threading import Thread
from libs.RegistrationAPI.KKTIX import KKTIX
from libs.RegistrationAPI.Meetup import Meetup
from parsing import Parsing
import io
from pathlib import Path
from terminaltables import DoubleTable
from termcolor import colored

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def wd_event_file(org_event, org):
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


def add_kktix_event(kktix_orgs):
    kktix_api = KKTIX()
    for org in kktix_orgs:
        org_event = kktix_api.get_meetup_info(org[2])
        wd_event_file(org_event, org)

# get user home path
# use absolute path check the files
# return mydir


def get_mydir():
    cmd = "echo $HOME"
    output = subprocess.check_output(cmd, shell=True)
    myhome = str(output.splitlines()).split("'")[1]
    my_dir = Path(myhome + "/.config/TGmeetup")
    if(my_dir.is_dir()):
        return str(my_dir)
    else:
        return None


def add_meetup_event(meetup_groups):
    mydir = get_mydir()
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
        wd_event_file(org_event, org)


def get_group_files():
    mydir = get_mydir()
    if mydir is None:
        print("Please run the steps as the following: \n \
               1. config API.cfg. \n 2. run 'sh install.sh'")
        pass
    cmd = "du -a " + mydir + "/community " + mydir + \
        "/conference | grep package.json | awk '{print $2}'"
    output = subprocess.check_output(cmd, shell=True)
    gf_all = []
    for gf in output.splitlines():
        try:
            gf_all.append(str(gf).split("'")[1])
        except BaseException:
            gf_all.append(str(gf))
    return(gf_all)


def Initial():
    meetup_groups = []
    kktix_groups = []
    all_files = get_group_files()
    for gfile in all_files:
        data = json.load(open(gfile))
        if data["registration"]["type"] == "meetup":
            meetup_groups.append(
                [gfile, data["name"], data["registration"]["url"]])
        elif data["registration"]["type"] == "kktix":
            kktix_groups.append(
                [gfile, data["name"], data["registration"]["url"]])
    return (meetup_groups, kktix_groups)


def update():
    (meetup_groups, kktix_groups) = Initial()
    t1 = Thread(target=add_meetup_event, args=(meetup_groups, ))
    t2 = Thread(target=add_kktix_event, args=(kktix_groups, ))
    t1.start()
    t2.start()


def print_result(result):
    tableData = []
    tableHead = ["Title(name)", "City", "Link / Meetup / Date"]
    tableData.append(tableHead)
    prevTitle = None
    for row in result:
        name = "("+row[0]+")"
        title = colored(row[1], 'green')
        city = colored(row[2], 'cyan')
        try:
            info = row[3:]
        except BaseException:
            info = None
        if len(info) == 0:
            tableData.append([title, city, ''])
            tableData.append([name, "", ''])
        else:
            meetup = info[0]
            date = info[1]
            link = info[2]
            date = colored(date, 'yellow')
            if title == prevTitle:
                tableData.append(['', '', date])
                tableData.append([name, '', meetup])
                tableData.append(['', '', link])
            else:
                tableData.append([title, city, date])
                tableData.append([name, '', meetup])
                tableData.append(['', '', link])
        prevTitle = title
    print(DoubleTable(tableData).table)


def main():
    "Using argparse to get events or search meetup"
    parser = argparse.ArgumentParser(description='TGmeetup')
    parser.add_argument(
        '-u',
        '--update',
        help='Update the events.json infomation.',
        action="store_true")
    parser.add_argument(
        '-c',
        '--country',
        type=str,
        help='This is a country code which follow ISO 3166-1 alpha-2.')
    parser.add_argument('-t', '--city', type=str, help='This is a city name.')
    parser.add_argument(
        '-n',
        '--name',
        type=str,
        help='This is a community short name.')
    parser.add_argument(
        '-k',
        '--keyword',
        type=str,
        help='This is a keyword of community. \
              This could help find the related community.')
    args = parser.parse_args()
    parsing = Parsing()
    if args.city is not None or args.keyword is not None or args.name is not None:
        if args.name is not None and args.city is None and args.keyword is None:
            # Show the group info (default country = Taiwan)
            result = parsing.show_organization_info(args.name, args.country)
            print(
                "The information of \"" +
                result["title"] +
                "\" in " +
                result["city"] +
                " (" +
                result["countrycode"] +
                ")")
            print(json.dumps(result, indent=2, sort_keys=False))
        elif args.city is not None and args.name is None and args.keyword is None:
            # List all the meetup in the city (default country = Taiwan)
            result = parsing.get_meetup_via_city(args.city, args.country)
            print_result(result)
        elif args.keyword is not None and args.city is None and args.name is None:
            # List all the meetup related to this keyword (default country =
            # Taiwan)
            result = parsing.show_meetup_via_keyword(
                args.keyword, args.country)
            print_result(result)
        else:
            print(
                "Please just use one option, such as name,keyword or city, \
                 and country option.")
            print("eg.")
            print("tgmeetup -k keypord\n tgmeetup -n name\ntgmetup -t Hsinchu")
    else:
        if args.update:
            update()
            print("Update all the meetup infomation.")
        else:
            # List all group with event in the country(default country = Taiwan).
            result = parsing.list_all_group_in_country(args.country)
            print_result(result)


if __name__ == '__main__':
    main()
