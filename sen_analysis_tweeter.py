#textblop helps performing the sentiment analysis
from textblob import TextBlob

#tweepy is the library for accessing twitter API
import tweepy

#The following four values you can obtaing once you create application account on tweeter
consumer_key= "your_twitter_consumer_key"
consumer_secret= "your_twitter_consumer_secret"

access_token= "your_twitter_consumer_access_token"
access_token_secret= "your_twitter_consumer_access_token_secret"

# authentication to login via twitter API
authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)

#setting set_access_token method on authentication
authentication.set_access_token(access_token, access_token_secret)


api_var = tweepy.API(authentication)

all_tweets = api_var.search("Putin")


#Polarity measures the sentiments whether negative or positive, and subjectivety measure how much of opinion as compared to how much factual a given text is

for tweets in all_tweets:
	print(tweets.text)
	tweet = TextBlob(tweets.text)
	total = tweet.sentiment
	print (total)
	print ("\n")


	
