#!/usr/bin/env python3
# coding=utf-8
import requests
import json
import time


class KKTIX():
    def get_meetup_info(self, org_url):
        url_name = (str(org_url).split("/")[2].split(".")[0])
        get_event_url = "https://" + url_name + ".kktix.cc/events.json"
        result = requests.get(get_event_url)
        events_info = result.json()["entry"]
        events_list = []
        if len(events_info) == 0:
            return None
        else:
            for event in events_info:
                if event["published"].split("T")[0] > time.strftime(
                        "%Y-%m-%d", time.localtime()):
                    events_list.append({
                        "name": event["title"],
                        "local_date": event["published"].split("T")[0],
                        "local_time": event["published"].split("T")[1].split(".")[0],
                        "link": event["url"]})
                else:
                    break
            if len(events_list) == 0:
                return None
            else:
                return events_list
