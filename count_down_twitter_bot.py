import tweepy, time, sys
from datetime import date
#from our keys module (keys.py), import the keys dictionary
from datetime import date

from Count_down_twitter_bot.keys import keys

def main():
    # Set keys dict
    keys_dict = keys

    # Get days to event
    current_time = time.gmtime()

    month = int((time.strftime("%m", current_time)))
    day = int((time.strftime("%d", current_time)))

    today = date(2016, month, day)
    event = date(2016, 9, 2)
    days_away = event - today
    days_away = (str(days_away))[0:3].replace(" ", "")


    # Create message
    message = days_away+" days to electric picnic. Shout out to @EPfestival and @Seatwave. Thanks for teaming up to rip off consumers and enable scalpers! #greed"

    # Post message
    post_tweet(message, keys_dict)

def post_tweet(message,keys_dict):

    # Get keys
    consumer_key = keys_dict.get("consumer_key")
    consumer_secret = keys_dict.get("consumer_secret")
    access_key = keys_dict.get("access_key")
    access_secret = keys_dict.get("accsss_secret")

    # Authenticte bot
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Push status update
    api.update_status(message)

if __name__ == '__main__':
    main()