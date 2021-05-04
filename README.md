# CoWIN vaccination slot availabilty checker and notifier
This is a small utility script to check for available vaccine slots in your location and receive a call to your mobile number when slots are available!

* Enter your pin code, mobile number and age limit (18-44/45+)
* Check availability of slots every x minutes 
* Receive a call on your mobile number when there is an available slot


## How to execute the script
This script uses python. Install python first if you haven't already

1. Download the repo as a zip and extract
2. Run `pip install -r requirements.txt`

3. Setting up a Twilio account:
   * Sign up for a free Twilio account at https://www.twilio.com/. Make sure you verify your own mobile number
   * On the dashboard, request a new mobile number. Click on "Choose mobile number" (it can be any country)
   * Copy your account_sid, your auth token and the Twilio mobile number

4. Open inputs.py in a text editor.
   * Paste these values one by one into the script
   * Enter the required inputs also

5. Run the script with `python main_script.py`
6. Keep the script running in the background

Please star the repo if you find the script useful!

## Disclaimer
This code is intended to be helpful amidst the covid-19 pandemic. It should not be misused with short time delays between requests made to coWIN's official website, https://www.cowin.gov.in/
