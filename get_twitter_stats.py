import tweepy
import os

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=os.environ['TWITTER_CONSUMER_KEY']
consumer_secret=os.environ['TWITTER_CONSUMER_SECRET']

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token=os.environ['TWITTER_OAUTH_TOKEN']
access_token_secret=os.environ['TWITTER_OAUTH_TOKEN_SECRET']

twitter_user=os.environ['TWITTER_USER']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
#print api.me().name
print api.get_user(twitter_user).friends_count
print api.get_user(twitter_user).followers_count
print api.get_user(twitter_user).statuses_count