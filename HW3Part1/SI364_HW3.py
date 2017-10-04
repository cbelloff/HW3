## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template
import json
app = Flask(__name__)
app.debug = True 
import requests

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform',methods= ['POST','GET'])
def artist_form():
    return render_template("artistform.html")

@app.route('/artistinfo',methods= ['POST','GET'])
def artist_info():
	if request.method == 'GET':
		result = request.args
		first = result.get('artist')
		params = {'term': first}
		x= requests.get('https://itunes.apple.com/search?', params=params)
		y= json.loads(x.text)
		return render_template("artist_info.html", objects=y['results'])

@app.route('/artistlinks',methods= ['POST','GET'])
def artist_links():
    return render_template("artist_links.html")

@app.route('/specific/song/<artist_name>')
def artist_name(artist_name):
	params= {}
	params['term'] = artist_name
	resp=requests.get('https://itunes.apple.com/search?', params=params)
	data=json.loads(resp.text)
	return render_template("artist_links.html")


if __name__ == '__main__':
    app.run()