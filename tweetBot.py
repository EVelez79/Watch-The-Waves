import tweepy,json
import configHandler

apiKeys = configHandler.readConfig()["API"]

consumerKey = apiKeys["ConsumerKey"]
consumerSecret = apiKeys["ConsumerSecret"]

accessToken = apiKeys["OAuthToken"]
accessTokenSecret = apiKeys["OAuthSecret"]

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

api.update_status("Testing123")
