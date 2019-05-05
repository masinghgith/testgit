# Wikibot
  This repo contains a wikibot which runs with Twilio WhatsApp
  This is deployed on pythonanywhere

# Requirements:
  Python 3.7
  Flask==1.0.2
  twilio==6.26.3
  wikipedia==1.4.0

# Steps:
  Setup Twilio Sandbox https://www.twilio.com/docs/sms/whatsapp/api
  Try Twilio Samples a few times without going into code building, once ready follow next steps
  Login to pythonanywhere, open bash console 
  Create virtual environment -> $ mkvirtualenv wikibot --python=/usr/bin/python3.7
  Git clone repository -> git clone https://github.com/masinghgith/wikibot.git
  Install dependencies from requirements.txt -> pip install -r requirements.txt --user
  Verify all required packages are installed in virtual environment ($ pip list)
  Create default web app
  Select virtual environment created on Web Page
  Delete flask_app.py and edit WSGI configuration file to use wikibot
 