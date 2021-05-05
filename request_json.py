import requests
from datetime import timedelta
from datetime import date
from inputs import pincode

today = date.today()
dates = []
responses = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

for i in range(0,71,7):
    dates.append((today + timedelta(days=i)).strftime('%d-%m-%Y'))

def request_json():
    for every_date in dates:
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}.'.format(pincode,every_date)
        r = requests.get(url, headers=headers)
        responses.append(r)
    return responses



