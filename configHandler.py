import json

CONFIG_DIR = "Resources/config.json"

def readConfig():
    # Load config.json
    strConfig = file(configDir, "r").read()

    # Parse to dictionary
    jsonConfig = json.loads(strConfig)

    return jsonConfig
