import tweepy
import json

#Twitter API INFO
oAuthToken = ""
oAuthSecret = ""

auth = tweepy.OAuthHandler(oAuthToken, oAuthSecret)

twp = tweepy.API(auth)

locationData = twp.trends_available()

trendingUS = [0];

#Find Trending Twitter Pages in US
for location in locationData:
    #print(str(location) + "\n")
    if "United States" in location.items()[6]:
        trendingUS.extend(location)

"""
for i in range(len(trendingUS)):
    print trendingUS[i]
"""
