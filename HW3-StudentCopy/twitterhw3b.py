# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "461609804-mLrHq4Jx5XE6RRcZDWNPL0sLAfN1T9yFUgMgfSX1"
access_token_secret = "19TBw847DydvdQRQTwTcUI6q5ZLS6HUvWOwZJy5bQbFp5"
consumer_key = "y69RWibGPebPJW99m02wzYGXY"
consumer_secret = "tzKFxQtHYCVOyrnYcHkGrHXggao0PD1bHGdLd0qodmOoJFS2XX"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('#Trump')

pol_count = 0
pol_total = 0

sub_count = 0 
sub_total = 0


for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)


	pol_count = pol_count + 1
	pol_total = pol_total + analysis.polarity

	sub_count = sub_count + 1
	sub_total = sub_total + analysis.subjectivity



		


avg_pol = pol_total/pol_count
avg_sub = sub_total/sub_count





print("Average subjectivity is " + str(avg_sub))
print("Average polarity is " + str(avg_pol))
