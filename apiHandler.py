import urllib, json, tweepy, datetime
from weather import Weather


#TODO create message format with the api data
def constructMessage():
    for spot in spotArray:
        # strftime formats the date into YYYYMMDD for the URL parameter
        #Accessing the spitcast api
        continue


Weather = Weather(unit="f")

class SpitCast:
    def __init__(self):
        # spots are Spitcast's ID for locations
        self.SPITCAST_URL = "http://api.spitcast.com/api/spot/forecast/"
        self.SPITCAST_URL_PARAMETER = "/?dval="


    def callApi(self, spot):
        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(days=1)
        urlToRequest = self.SPITCAST_URL + spot + self.SPITCAST_URL_PARAMETER + tomorrow.strftime('%Y%m%d')
        urlResponse = urllib.urlopen(urlToRequest)
        return json.loads(urlResponse.read())


class Twitter:
    def __init__(self, twitterConfig):
        self.config = twitterConfig
        self.twitter = self._setupTwitterAuth()


    #TODO implement tweeting
    def postTweet(self, message):
        self.twitter.update_status(message)


    def _setupTwitterAuth(self):
        consumerKey = self.config["ConsumerKey"]
        consumerSecret = self.config["ConsumerSecret"]
        accessToken = self.config["OAuthToken"]
        accessTokenSecret = self.config["OAuthSecret"]

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)

        return tweepy.API(auth)
