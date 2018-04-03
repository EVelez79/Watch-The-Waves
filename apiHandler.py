import urllib2, json, tweepy, datetime


#TODO create message format with the api data
def constructMessage():
    for spot in spotArray:
        # strftime formats the date into YYYYMMDD for the URL parameter
        #Accessing the spitcast api
        continue


def _httpGet(url):
    urlResponse = urllib2.urlopen(url)
    read = urlResponse.read()
    return read


class OpenWeather:
    OPEN_WEATHER_URL = "http://api.openweathermap.org/data/2.5/"
    KEY_PARAM = "&appid="
    ZIP_PARAM = "?zip="
    WEATHER_ENDPOINT = "weather"


    def __init__(self, key):
        self.key = key


    def getForecastByZip(self, zip):
        urlToRequest = self.OPEN_WEATHER_URL + self.WEATHER_ENDPOINT + self.ZIP_PARAM + str(zip) + self.KEY_PARAM + self.key
        forecast = json.loads(_httpGet(urlToRequest))
        return forecast


class SpitCast:
    FORECAST_PATH = "/spot/forecast"  # suffix: spot
    TEMPERATURE_PATH = "/county/water-temperature"  # suffix: countyName
    SPITCAST_URL = "http://api.spitcast.com/api"
    SPITCAST_URL_PARAMETER = "/?dval="


    def __init__(self):
        pass


    #currently all forecasts are only one day ahead
    #TODO add variable timedelta for the forecast
    def getForecast(self, spot):
        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(days=1)
        urlToRequest = self.SPITCAST_URL + self.FORECAST_PATH + "/" + spot + self.SPITCAST_URL_PARAMETER + tomorrow.strftime('%Y%m%d')
        urlResponse = json.loads(_httpGet(urlToRequest))

        return urlResponse


    #error 500 when requesting for los-angeles
    def getWaterTemp(self, spot):
        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(days=1)

        urlToRequest = self.SPITCAST_URL + self.TEMPERATURE_PATH + "/" + spot +"/"
        u = _httpGet(urlToRequest)
        urlResponse = json.loads(u)

        return urlResponse


class Twitter:
    def __init__(self, twitterConfig):
        self.config = twitterConfig
        self.twitter = self._setupTwitterAuth()


    #imagePath is a string
    def postTweet(self, message, imagePath=None):
        if imagePath == None:
            self.twitter.update_status(message)
        else:
            self.twitter.update_with_media(imagePath, message)


    def _setupTwitterAuth(self):
        consumerKey = self.config["ConsumerKey"]
        consumerSecret = self.config["ConsumerSecret"]
        accessToken = self.config["OAuthToken"]
        accessTokenSecret = self.config["OAuthSecret"]

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)

        return tweepy.API(auth)
