import apiHandler, datetime, urllib, json

CONFIG_DIR = "Resources/config.json"
DATABASE_DIR = "/Data/"

config = json.loads(open(CONFIG_DIR, "r").read())

spotArray = config["Locations"]
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

twitter = apiHandler.Twitter(config["TwitterAPI"])
