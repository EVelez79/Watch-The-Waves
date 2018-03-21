import apiHandler, configHandler, json, time, threading
from datetime import timedelta, datetime

config = configHandler.readConfig()
idArray = config["Locations"]["IDs"]
jsonDict = {}

SPITCAST_API = apiHandler.SpitCast()

def main():
    try:
        update_thread = threading.Thread(target = get_new_forecasts, name = "update thread")
    except:
        print("Exception when creating thread object")

    update_thread.start()
    time.sleep(30)

    for name in range(0,1):
        SPITCAST_API.construct_message(jsonDict[idArray[name]["Name"]], get_hour())


def get_new_forecasts():
    while True:
        for location in range(0, 1):
            jsonData = SPITCAST_API.get_forecast(idArray[location]["SpitCast"])
            name = idArray[location]["Name"]
            jsonDict[name] = jsonData

        time.sleep(86400)


def get_hour():
    hourString = datetime.now() + timedelta(hours=3)
    hourString = hourString.strftime("%I%p")

    if hourString[0] is "0":
        newHourString = hourString[1:]
        return newHourString
    else:
        return hourString


main()
