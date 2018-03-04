import apiHandler, configHandler, datetime, urllib, json

config = configHandler.readConfig()
spotArray = config["SpitCastAPI"]["Locations"]  # spots are Spitcast's ID for locations
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

jsonDict = dict()

SPITCAST_URL = "http://api.spitcast.com/api"
FORECAST_PATH = "/spot/forecast/"  # suffix: spot
TEMPERATURE_PATH = "/county/water-temperature/"  # suffix: countyName

twitter = apiHandler.set_twitter_auth(config)

def get_data(spot, urlToRequest):
    urlResponse = urllib.urlopen(urlToRequest)
    return json.loads(urlResponse.read())


def write_json(responseData, fileToWriteTo):
    jsonFile = open("Resources/JSON Files/forecast.txt", "w+")
    json.dump(responseData, jsonFile)
    jsonFile.close()


def get_forecast():
    for spot in spotArray:
        urlToRequest = SPITCAST_URL + FORECAST_PATH + spot
        return get_data(spot, urlToRequest)


def main():
    responseData = get_forecast()
    write_json(responseData)

main()
