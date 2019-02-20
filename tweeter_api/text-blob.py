from textblob import TextBlob

analysis = TextBlob("good morning asshole")

print(analysis.sentiment.polarity)