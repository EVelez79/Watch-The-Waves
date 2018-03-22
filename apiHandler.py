import urllib, json, tweepy, configHandler

class SpitCast:
    def __init__(self):
        # spots are Spitcast's ID for locations
        self.SPITCAST_URL = "http://api.spitcast.com/api/spot/forecast/"
        self.SPITCAST_URL_PARAMETER = "/?dval="
        self.TWITTER_API = Twitter()


    def get_forecast(self, spot):
        urlToRequest = self.SPITCAST_URL + spot + self.SPITCAST_URL_PARAMETER
        urlResponse = urllib.urlopen(urlToRequest)
        return json.loads(urlResponse.read())


    #TODO create message format with the api data
    def construct_message(self, jsonData, hour):
        for index, entry in enumerate(jsonData):
            if entry["hour"] == hour:
                name = entry["spot_name"]
                waveSize = "%.2f" % entry["size"]
                wind = entry["shape_detail"]["wind"]
                swell = entry["shape_detail"]["swell"]
                message = "Forecast for "+name+" at "+hour+": "+"Wind is "+wind+", wave size is "+waveSize+" ft, swell is "+swell
                self.TWITTER_API.post_tweet(message)
                print("success")


class Twitter:
    def __init__(self):
        self.config = configHandler.readConfig()
        self.twitter = self._setupTwitterAuth()


    #TODO implement tweeting
    def post_tweet(self, message):
        self.twitter.update_status(message)


    def _setupTwitterAuth(self):
        consumerKey = self.config["TwitterAPI"]["ConsumerKey"]
        consumerSecret = self.config["TwitterAPI"]["ConsumerSecret"]
        accessToken = self.config["TwitterAPI"]["OAuthToken"]
        accessTokenSecret = self.config["TwitterAPI"]["OAuthSecret"]

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)

        return tweepy.API(auth)
