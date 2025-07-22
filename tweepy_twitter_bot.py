import os
from dotenv import load_dotenv
import tweepy as tw
import tkinter as tk # for GUI interface

# Load environment variables from .env file
load_dotenv()

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate account with tweepy
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

# Check if program is working
user = api.verify_credentials()
print(user.name)

