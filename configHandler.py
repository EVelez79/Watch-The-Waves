import json

configDir = "Resources/config.json"

def readConfig():
    strConfig = file(configDir, "r").read()

    jsonConfig = json.loads(strConfig)

    return jsonConfig
