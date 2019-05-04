from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import wikipedia
import re

app = Flask(__name__)

def wikisearch(word):
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

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    # Create reply
    msg = request.form.get('Body')
    resp = MessagingResponse()
    resp.message("MASIBOT: {}".format(wikisearch(msg)))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
