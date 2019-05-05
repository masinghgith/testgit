# A very simple Flask, Twilio WhatsApp Application for you to get started with...

from flask import Flask, request
import wikipedia
import re
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def fromwiki(word):
    ck = re.match("^[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*$", word)
    if ck:
        wsg='Valid Input'
    else:
        wsg='Invalid Characters'

    if word.isdigit():
        wsg='Only Numbers Entered'
    elif len(word) not in range(5,24):
        wsg='Length Out of Range'

    if wsg=='Valid Input':
        wikipedia.set_lang('en')
        results = wikipedia.search(word)
        # get first result
        if results:
            page = wikipedia.page(results[0])
            wsg = page.title + "\n" + page.url
        else:
            wsg = '`{}` ??????????????'.format(word)
        return wsg
    else:
        return wsg

@app.route('/sms', methods=["GET", "POST"])
def wiki_search():
    if request.method == "POST":
        msg = request.form.get('Body')
        resp = MessagingResponse()
        resp.message("WikiB: {}".format(fromwiki(msg)))
        return str(resp)
    else:
        return 'Hello from Flask!'
