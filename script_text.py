#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
from twilio.rest import Client
from datetime import date

# 1) Enter your twilio account sid, auth token, and the twilio number given on the dashboard.
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
twilio_number = "+19999999999"

client = Client(account_sid, auth_token)

# 2) Enter your pincode, mobile number and age(18/45). Default is 18.
pincode="99999"
mobile_number = "+919999999999"
age = 18

# 3) Enter the time interval for which you want the slots to be checked (in seconds) Default is 20 mins.
time_interval = 1200

today = date.today()
date = today.strftime('%d-%m-%Y')

url = \
    'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}.'.format(pincode,
        date)

send_msg = False

while True:
    r = requests.get(url)
    msg_body = ''
    for center in r.json()['centers']:
        for session in center['sessions']:
            if session['available_capacity'] > 0 \
                and session['min_age_limit'] == age:
                send_msg = True
                line = \
                    ('Available {} slots for {}+ in {} .'.format(session['available_capacity'
                     ], session['min_age_limit'], center['name']), )
                body = ''.join(line)
                msg_body += '\n' + body
    if send_msg:
        message = client.messages.create(body=msg_body,
                from_=twilio_number, to=mobile_number)
    time.sleep(time_interval)
