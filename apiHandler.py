import urllib, json, tweepy, configHandler, datetime

today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

SPITCAST_URL = "http://api.spitcast.com/api/spot/forecast/"
URL_PARAMETER = "/?dval="

config = configHandler.readConfig()

def constructMessage():
    spots = config["SpitCastAPI"]["Locations"]
    for spot in spots:
        urlToRequest = SPITCAST_URL + spot + URL_PARAMETER + tomorrow.strftime('%Y%m%d')
        urlResponse = urllib.urlopen(urlToRequest)
        responseData = json.loads(request.read())

def postTweet(message):
    twitter = None
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
