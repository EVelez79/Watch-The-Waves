import tweepy, json, requests
import configHandler, magicSeaweedHandler

config = configHandler.readConfig()

#get MagicSeaweed API keys and locationIds
magicSeaweedConfig = config["MagicSeaweed"]

magicSeaweedKey = magicSeaweedConfig["ApiKey"]
magicSeaweedLocationIds = magicSeaweedConfig["Locations"]

#get twitterAPI keys
twitterConfig = config"TwitterAPI"]

consumerKey = apiKeys["ConsumerKey"]
consumerSecret = apiKeys["ConsumerSecret"]

accessToken = apiKeys["OAuthToken"]
accessTokenSecret = apiKeys["OAuthSecret"]

#setup twitterAPI authentication
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

twitter = tweepy.API(auth)

#call magicSeaweedAPI
magicSeaweedData = magicSeaweedHandler.multipleLocationCall(magicSeaweedLocationIds)

#post a tweet
twitter.update_status("Testing123")
