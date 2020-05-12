# TextMe

## Description
TextMe is a simple Python/Twilio application that will send an SMS when a GET
endpoint is accessed.

#### Background
When I invoke a long-running command, I usually context switch and come back
later so I'm not waiting on it. Natively on OSX, notifying myself upon
completion is as easy as:
```
$ ./long-running-command.sh && say Command Done
```

This results in a robo-voice saying "command done." However, if you're like me,
sometimes you run long running processes on random servers. That is, servers
that can't run `say` (or if they could, you wouldn't be able to hear). If it's
a regular (i.e. non-random) server, you could install a notification script
that would alert via email, growl, push, SMS, or whatever else. However, if
it's something that needs to be installed, it's less useful.

TextMe started with that principle: no installation. Additionally, it had to
be a quick and easy to memorize command. The following:
```
$ ./long-running-command.sh && curl textderwiki.herokuapp.com
```

uses the TextMe app, installed on Heroku, to send me a text message when
`long-running-command.sh` has completed.




## Running on Heroku

#### Pre-requisites
1. Heroku account
1. [Heroku CLI tool](https://devcenter.heroku.com/articles/heroku-cli)
1. Twilio free/trial account



#### Installing
```
# create the Heroku app
heroku create textderwiki

# set environment variables
heroku config:set NUMBER_FROM=5555551212 NUMBER_TO=5558675309 TWILIO_ACCOUNT_SID=<redacted> TWILIO_AUTH_TOKEN=<redacted> -a textderwiki

# deploy to Heroku
git push heroku origin master

# invoke the service to send you an SMS
curl textderwiki.herokuapp.com?t=hello
```
