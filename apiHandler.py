    import urllib, json, tweepy, datetime

def post_tweet(message):
    if twitter is None:
        setTwitterAuth()


def set_twitter_auth(config):
    twitterConfig = config["TwitterAPI"]
    consumerKey = twitterConfig["ConsumerKey"]
    consumerSecret = twitterConfig["ConsumerSecret"]
    accessToken = twitterConfig["OAuthToken"]
    accessTokenSecret = twitterConfig["OAuthSecret"]

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    return tweepy.API(auth)
