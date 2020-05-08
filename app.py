import os
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)


TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", None)
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", None)
CLIENT = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route("/")
def textme():
    body = request.values.get("t", "SYN")
    CLIENT.messages.create(body=body, from_="6145052620", to="7405023073")
    return "OK"
