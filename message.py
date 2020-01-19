# USAGE
# python ball_tracking.py --video ball_tracking_example.mp4
# python ball_tracking.py

# import the necessary packages
import webbrowser
import os
from twilio.rest import Client
from pyimagesearch.shapedetector import ShapeDetector

from pynput.keyboard import Key, Controller


keyboard = Controller()

account_sid = 'AC190646d0b130afd7dbaebb29f0db6b22'
auth_token = 'ce5b2e58a960118631b5e9b8240554f7'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='I AM JACK I AM IN AN EMERGENCY: {38.520971, -121.748178}',
                              from_='+16072694132',
                              to='+14155289715'
                          )
TWIML_INSTRUCTIONS_URL = \
"http://static.fullstackpython.com/phone-calls-python.xml"

TWILIO_PHONE_NUMBER = "+16072694132"
number = "+16692558370"
client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")

print(message.sid)
