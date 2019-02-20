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

public_tweets = api.search(q='arsenal',count=100)


print(dir(public_tweets[0]))

print(public_tweets[0].text)

print(public_tweets[0]._json['created_at'])

print(len(public_tweets))



#for tweet in public_tweets:
#    print (tweet)