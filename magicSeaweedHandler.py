import requests,json

apiUrl = "http://magicseaweed.com/api/forecast/?spot_id="

#returns json as dictionary
def callApi(locationId):
    url = apiUrl + str(locationId)
    return json.loads(requests.get(url))

#takes an array of location Ids
def multipleLocationCall(locations):
    dataDict = {}
    for i in locations:
        dataDict[i] = callApi(i)
    return dataDict
