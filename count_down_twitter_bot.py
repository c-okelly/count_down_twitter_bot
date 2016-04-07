import tweepy, time, sys
#from our keys module (keys.py), import the keys dictionary
from Count_down_twitter_bot.keys import keys

keys_dict = keys

def post_tweet(message,keys_dict):
    auth = tweepy.OAuthHandler(keys_dict.get("acces_key"), keys_dict.get("accss_secret"))
    auth.set_access_token(keys_dict.get("consumer_secret"), keys_dict.get("consumer_key"))
    api = tweepy.API(auth)


    api.update_status(message)
    time.sleep(15)#Tweet every 15 minutes