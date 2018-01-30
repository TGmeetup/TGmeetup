#!/usr/bin/env python3
# coding=utf-8
import requests
import time
import json
import geocoder


class KKTIX():
    def get_meetup_info(self, gfile, org_url):
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
                    data = json.load(open(gfile))
                    g = geocoder.google(data["city"])
                    while g.latlng is None:
                        g = geocoder.google(data["city"])
                    events_list.append({
                        "name": event["title"],
                        "local_date": event["published"].split("T")[0],
                        "local_time": event["published"].split("T")[1].split(".")[0],
                        "local_city": data["city"],
                        "geocodeFromGroup": "true",
                        "geocode": {
                            "lat": g.latlng[0],
                            "lng": g.latlng[1]
                        },
                        "link": event["url"]})
                else:
                    break
            if len(events_list) == 0:
                return None
            else:
                return events_list
