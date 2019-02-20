import tweepy

from pprint import pprint

consumer_key = 'M79jyuM8cWJC3MBLZMT1LAwft'

consumer_secret = 'bk6Ukwej6Dd42mU3Hq4wgeBbjlZ5qFekHfCqTQjkRaxlQgKu6Y'

access_token = '897799694440640513-ZsA5Whc5OHKpYCu1oumrf2EQ8SViUkl'

access_token_secret = 'YAPBvOFG2GAxigo3yG13Ca6HpOQIJczgjZqIWscH3VJBN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()

tweet_id = 1097779971832119296

public_tweets = api.search(q='to:KenyanTraffic',since_id=tweet_id,count=3000)

#public_tweets = api.user_timeline(screen_name='goal',since_id=tweet_id)


replies = []

'''
for tweet in public_tweets:
	print(tweet.in_reply_to_status_id)
'''

for tweet in public_tweets:
	if tweet.in_reply_to_status_id == tweet_id:
		replies.append(tweet.text)
		print(tweet.text,tweet._json['created_at'])

print(len(replies))

'''
#print(dir(replies[0]))

#print(replies[0]._json['created_at'])

print(len(replies))


tweet = api.get_status("1097435552050282496")

print(dir(tweet))

print(tweet.id_str)

#print(dir(tweet.user))

print(tweet.author.screen_name)
'''

