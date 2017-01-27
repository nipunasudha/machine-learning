import tweepy
from textblob import TextBlob

consumer_key = "ZvXGTU4F371GICUm6Tl4CdxIU"
consumer_secret = "bC2tc8E8At8BRNxVZ001ct94R4AbEex8HOoqJHXgZzcgmC46fK"

access_token = "2889645672-lELHuGWhUbLnHIUfWKS5iLffqeVEHIdvRDE6FFP"
access_token_secret = "ubD9oUAmsqQrEvLsWOF2FLmqfoD3xteYITLD6C8vOiIOH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text + "\n")
    analysis = TextBlob(tweet.text)
    print(str(analysis.sentiment) + "\n-------------------------")
