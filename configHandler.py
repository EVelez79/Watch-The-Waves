import json

jsonDir = "Resources/config.json"

def readConfig():
    #with open('/Resources/config.json') as json_data
    strConfig = file(jsonDir, "r").read()

    jsonConfig = json.loads(strConfig)

    return jsonConfig
