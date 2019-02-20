from flask import Flask,jsonify
from flask import request
#from tweeter_api.sentiments import Sentiment
from tweeter_api.google_cloud_nlp import Sentiment
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
	return 'tweet-meter'

@app.route('/search/',methods=['GET', 'POST'])
def search():
	sentiment = Sentiment(10)
	q = ''
	if request.method == 'GET': q = request.args.get('q','')
	if request.method == 'POST':q = request.get_json()['query']
	if q.startswith("https://"):
		res = sentiment.replies_analysis(tweet_url=q)
		return jsonify({'data':res})
	elif q != '':
		res = sentiment.tweets_analysis(query=q)
		return jsonify({'data':res})
	return jsonify({'data':[0,0,0]})


@app.errorhandler(500)
def server_error(error):
	return 500

@app.errorhandler(404)
def page_not_found(error):
	return 404


'''
if __name__=='__main__':
	app.run(debug=True, port=5000)
'''