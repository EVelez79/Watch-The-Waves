import urllib, json, tweepy, configHandler, datetime

config = configHandler.readConfig()
spots = config["SpitCastAPI"]["Locations"]
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

SPITCAST_URL = "http://api.spitcast.com/api/spot/forecast/"
URL_PARAMETER = "/?dval="
twitterConfig = config["TwitterAPI"]
consumerKey = twitterConfig["ConsumerKey"]
consumerSecret = twitterConfig["ConsumerSecret"]
accessToken = twitterConfig["OAuthToken"]
accessTokenSecret = twitterConfig["OAuthSecret"]

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

twitter = tweepy.API(auth)

def constructMessage():
    for spot in spots:
        # strftime formats the date into YYYYMMDD for the URL parameter
        urlToRequest = SPITCAST_URL + spot + URL_PARAMETER + tomorrow.strftime('%Y%m%d')
        urlResponse = urllib.urlopen(urlToRequest)
        responseData = json.loads(urlResponse.read())

def postTweet(message):
    if twitter is None:
        twitterConfig = config["TwitterAPI"]
        consumerKey = twitterConfig["ConsumerKey"]
        consumerSecret = twitterConfig["ConsumerSecret"]

        accessToken = twitterConfig["OAuthToken"]
        accessTokenSecret = twitterConfig["OAuthSecret"]

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)

        twitter = tweepy.API(auth)

    twitter.update_status(message)
