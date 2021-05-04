import time
from twilio.rest import Client
from inputs import *
from request_json import *

client = Client(account_sid, auth_token)

request_no = 0
availablility = False

while True:
    responses = request_json()
    request_no += 1
    print("Request no:",request_no)
    for response in responses:
        for center in response.json()['centers']:
            for session in center['sessions']:
                if session['available_capacity'] > 0 and session['min_age_limit'] == age:
                    availablility = True
    if availablility == True:
        call = client.calls.create(twiml='<Response><Say>Vaccine slot is available. Go to cowin.gov.in to book your slot.</Say></Response>', to=mobile_number, from_=twilio_number)
    time.sleep(time_interval)
    