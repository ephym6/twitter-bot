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
try:
    user = api.verify_credentials()
    print(user.name)
except tw.TweepyException as e:
    print(f"Authentication Error: {e}")
except Exception as e:
    print(f"Error: {e}")

# Building the Bot
# This bot is meant to:
#
# 1. Follow everyone following you.
# 2. Favorite and Retweet a Tweet based on keywords.
# 3. Reply to a user based on a keyword.

# loop through your followers and then follow each one.
# for follower in tw.Cursor(api.get_followers).items():
#     if not follower.following:  # Only follow if not already following
#         follower.follow()
#         print(f"Following {follower.name}")
#     else:
#         print(f"Already following {follower.name}")

def bot_function():
    search_term = "Keyword"
    number_of_tweets = "Number of tweets you wish to interact with"
    for tweet in tw.Cursor(api.search_tweets, search_term).items(number_of_tweets):
        try:
            # Like tweet
            if not tweet.favorited:
                tweet.create_favorite()
                print(f"Liked {tweet.user.name}'s tweet")

            # Retweet
            if not tweet.retweeted:
                tweet.retweet()
                print(f"Retweeted {tweet.user.name}'s tweet")

        except tw.TweepyException as tweep_error:
            print(f"Twitter API Error: {str(tweep_error)}")
        except StopIteration:
            break
