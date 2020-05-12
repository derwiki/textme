import os
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)


NUMBER_FROM = os.environ.get("NUMBER_FROM", None)
NUMBER_TO = os.environ.get("NUMBER_TO", None)
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", None)
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", None)
CLIENT = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route("/")
def textme():
    body = request.values.get("t", "SYN")
    CLIENT.messages.create(body=body, from_=NUMBER_FROM, to=NUMBER_FROM)
    return "OK"
