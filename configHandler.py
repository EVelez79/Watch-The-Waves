import json

configDir = "Resources/config.json"

def readConfig():
    #load config.json
    strConfig = file(configDir, "r").read()

    #parse to dictionary
    jsonConfig = json.loads(strConfig)

    return jsonConfig
