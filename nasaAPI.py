import json
import urllib.request

from flask import Flask, render_template, request

app = Flask(__name__)

#Home Page
@app.route('/')
def home():
        #Default API key and URL
        url = 'https://api.nasa.gov/planetary/apod?'
        apiKey = 'DEMO_KEY'

        #Build image URL to pass to template
        imgUrl = buildURL(url, apiKey)
        
        #Return home.html template and pass the image URL
        return render_template('home.html', imgUrl=imgUrl)

@app.route('/testKey', methods=['POST'])
def testKey():
        #Getting URL from form
        url = request.form['urlField']
        
        #Getting API key input from form
        apiKey = request.form['apikey']

        imgUrl = buildURL(url, apiKey)     
        return render_template('home.html', imgUrl=imgUrl)

def buildURL(url, apiKey):
        urlObj = urllib.request.urlopen(url + 'api_key=' + apiKey)
        read = urlObj.read()
        decode = json.loads(read.decode('utf-8'))

        #Get image URL from json object
        imgUrl = decode['url']
        return imgUrl
