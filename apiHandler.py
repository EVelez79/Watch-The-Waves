import urllib, json, tweepy, configHandler, datetime

config = configHandler.readConfig()

twitterConfig = config["TwitterAPI"]
consumerKey = twitterConfig["ConsumerKey"]
consumerSecret = twitterConfig["ConsumerSecret"]
accessToken = twitterConfig["OAuthToken"]
accessTokenSecret = twitterConfig["OAuthSecret"]

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

twitter = tweepy.API(auth)

# spots are Spitcast's ID for locations
spotArray = config["SpitCastAPI"]["Locations"]
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

SPITCAST_URL = "http://api.spitcast.com/api/spot/forecast/"
URL_PARAMETER = "/?dval="
TWEET_INTRO = "Tomorrow's surf forecast for "
AT = " at "
WIND = "Wind condition: "
WAVE = "Wave height: "


def constructMessage():
    for spot in spotArray:
        responseData = getForecast

        spotName = responseData[12]["spot_name"]
        forecastTime = responseData[12]["hour"]
        windCondition = responseData[12]["shape_detail"]["wind"]
        waveHeight = responseData[12]["size"]

        tweet = TWEET_INTRO + spotName + AT + str(forecastTime) + ". " + WIND + windCondition + ", " + WAVE  + str(waveHeight) + "ft"

        postTweet(tweet)

        time.sleep(480)


def getForecast():
    responseData = list()
    for spot in spotArray:
        # strftime formats the date into YYYYMMDD for the URL parameter
        urlToRequest = SPITCAST_URL + spot + URL_PARAMETER + tomorrow.strftime('%Y%m%d')
        urlResponse = urllib.urlopen(urlToRequest)
        rawData = json.loads(urlResponse.read())
        responseData.append(rawData)
    return responseData


def postTweet(message):

    twitter.update_status(message)
