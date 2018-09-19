#!/usr/bin/env python3
# coding=utf-8
import requests
import time
import json
from geopy.geocoders import Nominatim


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
                    geolocator = Nominatim(user_agent="TGmeetup")
                    try:
                        g = geolocator.geocode(data["city"])
                        while g.latitude is None:
                            g = geolocator.geocode(data["city"])
                    except BaseException:
                        g = geolocator.geocode(data["city"])
                        while g.latitude is None:
                            g = geolocator.geocode(data["city"])
                    events_list.append({
                        "name": event["title"],
                        "local_date": event["published"].split("T")[0],
                        "local_time": event["published"].split("T")[1].split(".")[0],
                        "location": event["content"].split("：")[2],
                        "local_city": data["city"],
                        "geocodeFromGroup": "true",
                        "geocode": {
                            "lat": g.latitude,
                            "lng": g.longitude
                        },
                        "link": event["url"]})
                else:
                    break
            if len(events_list) == 0:
                return None
            else:
                if len(events_list) > 3:
                    sorted(events_list, key=lambda k: k['local_date'], reverse=True)
                return events_list
