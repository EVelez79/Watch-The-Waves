import urllib, json, tweepy, configHandler, datetime

config = configHandler.readConfig()
# spots are Spitcast's ID for locations
spotArray = config["SpitCastAPI"]["Locations"]
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

SPITCAST_URL = "http://api.spitcast.com/api/spot/forecast/"
URL_PARAMETER = "/?dval="

def constructMessage():
    for spot in spotArray:
        # strftime formats the date into YYYYMMDD for the URL parameter
        urlToRequest = SPITCAST_URL + spot + URL_PARAMETER + tomorrow.strftime('%Y%m%d')
        urlResponse = urllib.urlopen(urlToRequest)
        responseData = json.loads(urlResponse.read())

def postTweet(message):
    if twitter is None:
        setTwitterAuth()

def setTwitterAuth():
    twitterConfig = config["TwitterAPI"]
    consumerKey = twitterConfig["ConsumerKey"]
    consumerSecret = twitterConfig["ConsumerSecret"]
    accessToken = twitterConfig["OAuthToken"]
    accessTokenSecret = twitterConfig["OAuthSecret"]

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    twitter = tweepy.API(auth)
