#!/usr/bin/env python3
# coding=utf-8
import subprocess
import json


class Parsing():
    def get_mydir(self):
        cmd = "find ~/ -name TGmeetup | sed -n '1p'"
        output = subprocess.check_output(cmd, shell=True)
        try:
            mydir = str(output.splitlines()).split("'")[1]
        except BaseException:
            mydir = str(output.splitlines())
        return mydir

    def get_org_files(self, country):
        mydir = self.get_mydir()
        cmd = "du -a " + mydir + "/community " + mydir + "/conference | grep " + \
            country + " | grep package.json | awk '{print $2}'"
        organization_file = subprocess.check_output(cmd, shell=True)
        all_org = []
        for org in organization_file.splitlines():
            try:
                all_org.append(str(org).split("'")[1])
            except BaseException:
                all_org.append(str(org))
        return all_org

    def show_organization_info(self, name, country=None):
        if country is None:
            country = "tw"
        mydir = self.get_mydir()
        cmd = "du -a " + mydir + "/community " + mydir + "/conference | grep " + \
            country + "/" + name + "/package.json | awk '{print $2}'"
        organization_file = subprocess.check_output(cmd, shell=True)
        data = json.load(
            open(str(organization_file.splitlines()).split("'")[1]))
        return data

    def get_meetup_via_city(self, city, country=None):
        if country is None:
            country = "tw"
        all_org = self.get_org_files(country)
        list_all = []
        for org_file in all_org:
            org_data = json.load(open(org_file))
            org_event = None
            if org_data["city"] == city:
                try:
                    org_event = json.load(
                        open(
                            org_file.replace(
                                "package.json",
                                "events.json")))
                except BaseException:
                    org_event = None
                if org_event is None:
                    list_all.append(
                        [org_data["name"], org_data["title"], org_data["city"]])
                else:
                    list_all.append([org_data["name"],
                                     org_data["title"],
                                     org_data["city"],
                                     org_event[0]["name"],
                                     org_event[0]["local_date"],
                                     org_event[0]["link"]])
        return list_all

    def show_meetup_via_keyword(self, keyword, country=None):
        if country is None:
            country = "tw"
        all_org = self.get_org_files(country)
        list_all = []
        for org_file in all_org:
            org_data = json.load(open(org_file))
            if org_data["keywords"]:
                for k in org_data["keywords"]:
                    if k == keyword:
                        try:
                            org_event = json.load(
                                open(
                                    org_file.replace(
                                        "package.json",
                                        "events.json")))
                        except BaseException:
                            org_event = None
                        if org_event is None:
                            list_all.append(
                                [org_data["name"], org_data["title"], org_data["city"]])
                        else:
                            list_all.append([org_data["name"],
                                             org_data["title"],
                                             org_data["city"],
                                             org_event[0]["name"],
                                             org_event[0]["local_date"],
                                             org_event[0]["link"]])
            else:
                continue
        return list_all

    def list_all_group_in_country(self, country=None):
        if country is None:
            country = "tw"
        all_org = self.get_org_files(country)
        list_all = []
        for org_file in all_org:
            org_data = json.load(open(org_file))
            try:
                org_event = json.load(
                    open(
                        org_file.replace(
                            "package.json",
                            "events.json")))
            except BaseException:
                org_event = None
            if org_event is None:
                list_all.append(
                    [org_data["name"], org_data["title"], org_data["city"]])
            else:
                list_all.append([org_data["name"],
                                 org_data["title"],
                                 org_data["city"],
                                 org_event[0]["name"],
                                 org_event[0]["local_date"],
                                 org_event[0]["link"]])
        return list_all
