import urllib, json, tweepy, configHandler, datetime

config = configHandler.readConfig()
# spots are Spitcast's ID for locations
spotArray = config["SpitCastAPI"]["Locations"]
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

SPITCAST_URL = "http://api.spitcast.com/api/spot/forecast/"
URL_PARAMETER = "/?dval="

class Twitter:
    def __init__(twitterConfig):
        self.config = twitterConfig
        self.twitter = self._setupTwitterAuth()


    def constructMessage():
        for spot in spotArray:
            # strftime formats the date into YYYYMMDD for the URL parameter
            urlToRequest = SPITCAST_URL + spot + URL_PARAMETER + tomorrow.strftime('%Y%m%d')
            urlResponse = urllib.urlopen(urlToRequest)
            responseData = json.loads(urlResponse.read())

    #TODO implement the actual
    def postTweet(message):
        setTwitterAuth()
        api.update_status(message)

    def _setupTwitterAuth():
        twitterConfig = self.config["TwitterAPI"]
        consumerKey = self.config["ConsumerKey"]
        consumerSecret = self.config["ConsumerSecret"]
        accessToken = self.config["OAuthToken"]
        accessTokenSecret = self.config["OAuthSecret"]

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)

        return tweepy.API(auth)
