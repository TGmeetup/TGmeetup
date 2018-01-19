#!/usr/bin/env python3
# coding=utf-8
import requests


class Meetup():
    def __init__(self, url, key, secret, refresh_token):
        self.url = url
        self.key = key
        self.secret = secret
        self.refresh_token = refresh_token

    def refresh_access_token(self):
        header = {'Content-type': 'application/x-www-form-urlencoded'}
        api_url = 'https://secure.meetup.com/oauth2/access'
        payload = "client_id=" + self.key + "&client_secret=" + self.secret + \
            "&grant_type=refresh_token&refresh_token=" + self.refresh_token
        result = requests.post(api_url, headers=header, data=payload)
        return result.json()["access_token"]

    def get_meetup_info(self, access_token, org_url):
        url_name = (str(org_url).split("/")[3])
        get_event_url = "https://api.meetup.com/" + \
            url_name + "/events?access_token=" + access_token
        result = requests.get(get_event_url)
        events_info = result.json()
        events_list = []
        if len(events_info) == 0:
            return None
        else:
            for event in events_info:
                events_list.append({
                    "name": event["name"],
                    "local_date": event["local_date"],
                    "local_time": event["local_time"],
                    "location": event["venue"]["name"],
                    "local_city": event["venue"]["city"],
                    "link": event["link"]})
            return events_list
