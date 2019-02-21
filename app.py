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
	query = ''
	if request.method == 'GET': query = request.args.get('query','')
	if request.method == 'POST':query = request.get_json()['query']
	if query.startswith("https://"):
		res = sentiment.replies_analysis(tweet_url=query)
		return jsonify(res)
	elif query != '':
		res = sentiment.tweets_analysis(query=query)
		return jsonify(res)
	return jsonify({'negative':0,'positive':0,'neutral':0})


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