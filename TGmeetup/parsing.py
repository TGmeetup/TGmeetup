#!/usr/bin/env python3
# coding=utf-8
import subprocess
import json
import os
from pathlib import Path

class Parsing():
    def get_mydir(self):
        cmd = "echo $HOME"
        output = subprocess.check_output(cmd, shell=True)
        myhome = str(output.splitlines()).split("'")[1]
        my_dir = Path(myhome+"/.config/TGmeetup")
        if(my_dir.is_dir()):
            print(os.path.exists(str(my_dir)+"/API.cfg"))
            print(os.path.exists(str(my_dir)+"/community/"))
            print(os.path.exists(str(my_dir)+"/conference/"))
            return str(my_dir)
        else:
            return None

    def listdata(self, org_data, org_event):
        org_list = []
        if org_event is None:
            org_list.append(
                [org_data["name"], org_data["title"], org_data["city"]])
        else:
            event_num = len(org_event) - 1
            org_list.append([org_data["name"],
                             org_data["title"],
                             org_data["city"],
                             org_event[event_num]["name"],
                             org_event[event_num]["local_date"],
                             org_event[event_num]["link"]])
        return org_list[0]

    def get_org_event(self, org_file):
        try:
            org_event = json.load(open(org_file.replace("package.json", "events.json")))
        except BaseException:
            org_event = None
        return org_event

    def get_org_files(self, country):
        mydir = self.get_mydir()
        if mydir == None:
            print("Please run the steps as the following: \n 1. cionfig API.cfg. \n 2. run 'tgmeetup install'")
            pass
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
        if mydir == None:
            print("Please run the steps as the following: \n 1. cionfig API.cfg. \n 2. run 'tgmeetup install'")
            pass
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
                org_event = self.get_org_event(org_file)
                list_all.append(self.listdata(org_data, org_event))
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
                        org_event = self.get_org_event(org_file)
                        list_all.append(self.listdata(org_data, org_event))
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
            org_event = self.get_org_event(org_file)
            list_all.append(self.listdata(org_data, org_event))
        return list_all
