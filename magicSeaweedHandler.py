import requests,json

apiUrl = "http://magicseaweed.com/api/APIKEY/forecast/?spot_id="

#returns json as dictionary
def callApi(apiKey, locationId):
    #insert apikey and append locationid
    url = apiUrl.replace("APIKEY", apiKey) + str(locationId)
    return json.loads(requests.get(url))

#takes an array of location Ids
def multipleLocationCall(apiKey, locations):
    dataDict = {}
    for i in locations:
        dataDict[i] = callApi(apiKey, i)
    #dataDict keys are strings
    return dataDict
