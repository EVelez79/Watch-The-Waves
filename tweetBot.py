import apiHandler, datetime, json

CONFIG_DIR = "Resources/config.json"
DATABASE_DIR = "/Data/"

config = json.loads(open(CONFIG_DIR, "r").read())

locations = config["Locations"]

spitcast = apiHandler.SpitCast()
weather = apiHandler.OpenWeather(config["OpenWeatherAPI"]["Key"])

twitter = apiHandler.Twitter(config["TwitterAPI"])