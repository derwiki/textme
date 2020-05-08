import os
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)


TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", None)
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", None)
CLIENT = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_SID)


@app.route("/")
def textme():
    CLIENT.Messages.create(
        body=request.values["t"], from_="6145052620", to="7405023073"
    )
    return "OK"
