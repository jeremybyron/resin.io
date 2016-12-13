#!/usr/bin/python

from flask import Flask, request, redirect

from num2words import num2words
from subprocess import call

import twilio.twiml
import urllib, pycurl, os

def downloadFile(url, fileName):
        fp = open(fileName, "wb")
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.WRITEDATA, fp)
        curl.perform()
        curl.close()
        fp.close()

def speakSpeechFromText(phrase):
	cmd_beg= 'espeak '
	cmd_end= 'aplay Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
	cmd_out= '--stdout > Text.wav ' # To store the voice file

	#Replacing ' ' with '_' to identify words in the text entered
	text = phrase.replace(' ', '_')

	#Calls the Espeak TTS Engine to read aloud a Text
	call([cmd_beg+cmd_out+text], shell=True)
	call([cmd_end], shell=True)

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
        """Respond to incoming calls with a simple text message."""
        sms = request.args.get('Body')
        if not sms == "": #if sms is not none, if sms exist
                speakSpeechFromText(sms)

        resp = twilio.twiml.Response()
        #resp.message("Hello, Mobile Monkey")
        return str(resp)

if __name__ == "__main__":
	print "Hello twilio"
        app.run( host='0.0.0.0', debug=True, port = 80)
