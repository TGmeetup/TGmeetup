#!/usr/bin/env python3
# coding=utf-8

import os
import json
import time
import argparse
import configparser
import subprocess
from threading import Thread
from libs.RegistrationAPI.KKTIX import *
from libs.RegistrationAPI.Meetup import *
from parsing import *
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def add_kktix_event(kktix_orgs):
    kktix_api = KKTIX()
    for org in kktix_orgs:
        org_event = kktix_api.get_meetup_info(org[2])
        if org_event is None:
            try:
                os.remove(org[0].replace("package.json", "events.json"))
            except BaseException:
                continue
        else:
            with io.open(org[0].replace("package.json", "events.json"), 'w', encoding='utf8') as outfile:
                str_ = json.dumps(org_event,
                                  indent=2, sort_keys=True,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))


def add_meetup_event(meetup_groups):
    config = configparser.ConfigParser()
    config.read('API.cfg')
    meetup_api = Meetup(
        config['MEETUP_API']['API_URL'],
        config['MEETUP_API']['API_KEY'],
        config['MEETUP_API']['client_secret'],
        config['MEETUP_API']['refresh_token'])
    access_token = meetup_api.refresh_access_token()
    for org in meetup_groups:
        org_event = meetup_api.get_meetup_info(access_token, org[2])
        if org_event is None:
            try:
                os.remove(org[0].replace("package.json", "events.json"))
            except BaseException:
                continue
        else:
            with io.open(org[0].replace("package.json", "events.json"), 'w', encoding='utf8') as outfile:
                str_ = json.dumps(org_event,
                                  indent=2, sort_keys=True,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))


def get_group_files():
    output = subprocess.check_output(
        "du -a ../community ../conference | grep package.json | awk '{print $2}'",
        shell=True)
    gf_all = []
    for gf in output.splitlines():
        gf_all.append(str(gf).split("'")[1])
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
    print("Name\tTitle\tCity\n")
    print("\t\tMeetup\tDate\n")
    print("\t\tLink\n")
    print("==========================================================\n")
    for r in result:
        if len(r) > 3:
            print(r[0] + "\t" + r[1] + "\t" + r[2] + "\n")
            print("\t\t\t\t" + r[3] + "\t" + r[4] + "\n")
            print("\t\t\t\t" + r[5] + "\n")
        else:
            print(r[0] + "\t" + r[1] + "\t" + r[2] + "\n")


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
        help='This is a keyword of community. This could help find the related community.')
    args = parser.parse_args()
    if args.update:
        update()
        print("Update all the meetup infomation.")
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
            print(json.dumps(result, indent=2))
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
                "Please just use one option, such as name,keyword or city, and country option.")
            print("eg.")
            print("tgmeetup -k keypord\n tgmeetup -n name\ntgmetup -t Hsinchu")
    else:
        # List all group with event in the country(default country = Taiwan).
        result = parsing.list_all_group_in_country(args.country)
        print_result(result)


if __name__ == '__main__':
    main()
