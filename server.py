from flask import Flask
from flask import request
#from tweeter_api.sentiments import Sentiment
from tweeter_api.google_cloud_nlp import Sentiment
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
	return 'tweet-meter'

@app.route('/search/')
def search():
	sentiment = Sentiment(10)
	q = request.args.get('q','')
	if q.startswith("https://"):
		res = sentiment.replies_analysis(tweet_url=q)
		return json.dumps({'data':res})
	elif q != '':
		res = sentiment.tweets_analysis(query=q)
		return json.dumps({'data':res})
	return json.dumps({'data':[0,0,0]})


@app.errorhandler(500)
def server_error(error):
	return 500

@app.errorhandler(404)
def page_not_found(error):
	return 404