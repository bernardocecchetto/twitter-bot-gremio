import tweepy
import schedule
from bot_gremio.credentials import *

def run():
    # Authenticate to Twitter
    client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_SECRET)


    response = client.create_tweet(text='GRÊMIO')



schedule.every().day.at("19:03").do(run)
