import requests, json, tweepy
import configHandler

spitCastApiUrl = "http://api.spitcast.com/api/spot/forecast/"

config = configHandler.readConfig()

#takes an array of location Ids
def callSpitcastLocations():
    locations = config["SpitCastAPI"]["Locations"]
    dataDict = {}
    for i in locations:
        #http request and json parsing
        dataDict[i] = json.loads(requests.get(spitCastApiUrl + i).text)
    #dataDict keys are strings
    return dataDict


twitter = None
def postTweet(message):
    #initialize twitter if this is the first run
    if twitter is None:
        twitterConfig = config["TwitterAPI"]
        consumerKey = twitterConfig["ConsumerKey"]
        consumerSecret = twitterConfig["ConsumerSecret"]

        accessToken = twitterConfig["OAuthToken"]
        accessTokenSecret = twitterConfig["OAuthSecret"]

        auth = tweep.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)

        twitter = tweepy.API(auth)

    twitter.update_status(message)
