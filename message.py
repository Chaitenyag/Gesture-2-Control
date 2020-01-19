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

account_sid = 'A____'
auth_token = 'c______'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='I AM JACK I AM IN AN EMERGENCY: {38.520971, -121.748178}',
                              from_='+1',
                              to='+1'
                          )
TWIML_INSTRUCTIONS_URL = \
"http://static.fullstackpython.com/phone-calls-python.xml"

TWILIO_PHONE_NUMBER = "+1"
number = "+1"
client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")

print(message.sid)
