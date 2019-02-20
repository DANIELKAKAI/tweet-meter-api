from textblob import TextBlob 
from textblob.exceptions import NotTranslated
import tweepy
import re


class Sentiment():
	def __init__(self,count):
		self.count = count
		consumer_key = 'M79jyuM8cWJC3MBLZMT1LAwft'
		consumer_secret = 'bk6Ukwej6Dd42mU3Hq4wgeBbjlZ5qFekHfCqTQjkRaxlQgKu6Y'
		access_token = '897799694440640513-ZsA5Whc5OHKpYCu1oumrf2EQ8SViUkl'
		access_token_secret = 'YAPBvOFG2GAxigo3yG13Ca6HpOQIJczgjZqIWscH3VJBN'
		try:
			self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_token_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")
		
	def clean_tweet(self,tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def tweets_analysis(self,query):
		public_tweets = self.api.search(q=query,count=self.count)
		tweets = set([tweet.text for tweet in public_tweets])
		return self.analyze(tweets)

	def replies_analysis(self,tweet_url):
		tweet_id = self.get_tweet_id(tweet_url)
		tweet = self.api.get_status(str(tweet_id))
		query = 'to:'+tweet.author.screen_name
		tweets = self.api.search(q=query,since_id=tweet_id,count=self.count)
		replies = []
		for tweet in tweets:
			if tweet.in_reply_to_status_id == tweet_id:
				replies.append(tweet.text)
		return self.analyze(replies)

	def analyze(self,tweets):
		positive_count = 0
		negative_count = 0
		neutral_count = 0
		total = 1
		for tweet in tweets:
			analysis = TextBlob(tweet)
			try:
				analysis = analysis.translate(to='en')
			except NotTranslated:
				pass
			if analysis.sentiment.polarity >0:
				positive_count += 1
			elif analysis.sentiment.polarity==0:
				neutral_count += 1
			else:
				negative_count += 1
		total = positive_count+negative_count+neutral_count
		return [int(positive_count/total*100),int(neutral_count/total*100),int(negative_count/total*100)]

	def get_tweet_id(self,url):
		r = re.findall(r'\d+',url,re.M|re.I)
		return int(r[-1])

				



