# CoWIN vaccination slots checker and notifier
This is a small utility script to check for available vaccination slots in your location and receive a text message to your number when slots are available!

* Enter your pin code, mobile number and age
* Check availability of slots every 20 minutes
* Receive a text message on your mobile number when there is an available slot


## How to execute the script
This script uses python. Install python first if you haven't already
1) Download the repo as a zip and extract
2) Run `pip install -r requirements.txt`
3) Setting up a Twilio account:
  * Sign up for a free Twilio account at twilio.com
  * On the dashboard, request a new mobile number. Click on "Choose mobile number" (it can be any country)
  * Copy your account_sid, your auth token and the Twilio mobile number
4) Open script.py in a text editor
  * Paste these values one by one into the script
  * Enter the required inputs as given in the script
6) Run the script with `python script.py` and keep it running


Please star the repo if you find the script useful!

## Disclaimer
This code is intended to be helpful amidst the covid-19 pandemic. It should not be misused with short time delays between requests made to coWIN's official website. [cowin.gov.in]

1. A numbered list
              1. A nested numbered list
              2. Which is numbered
          2. Which is numbered
