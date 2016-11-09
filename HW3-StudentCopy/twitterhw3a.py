# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

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

img = "jetsnation.jpg"
txt = "#UMSI-206 #Proj3"

api.update_with_media(img,status=txt)
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search




print("""No output necessary""")