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

# Creating the GUI
# will take our inputs of the keyword you would like to search for and
# whether or not you would like to favorite a tweet.

root = tk.Tk()
# Labels
label_1 = tk.Label(root, text="Search")
E1 = tk.Entry(root, bd =5)
label_2 = tk.Label(root, text="Number of Tweets")
E2 = tk.Entry(root, bd =5)
label_3 = tk.Label(root, text="Response")
E3 = tk.Entry(root, bd =5)
label_4 = tk.Label(root, text="Reply")
E4 = tk.Entry(root, bd =5)
label_5 = tk.Label(root, text="Favorite")
E5 = tk.Entry(root, bd =5)
label_6 = tk.Label(root, text="Retweet")
E6 = tk.Entry(root, bd =5)
label_7 = tk.Label(root, text="Follow")
E7 = tk.Entry(root, bd =5)

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
    # call & store inputs
    get_e1()
    search = get_e1()
    get_e2()
    number_of_tweets = int(get_e2()) # convert to int
    get_e3()
    response = get_e3()
    get_e4()
    reply = get_e4()
    get_e5()
    favorite = get_e5()
    get_e6()
    retweet = get_e6()
    get_e7()
    follow = get_e7()

    search_term = search
    number_of_tweets = number_of_tweets
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

    # Reply to a user based on a keyword
    phrase = response
    for tweet in tw.Cursor(api.search_tweets, search_term).items(number_of_tweets):
        try:
            tweet_id = tweet.user.id
            username = tweet.user.screen_name
            api.update_status(status=f"@{username} {phrase}", in_reply_to_status_id=tweet_id)
            print(f"Replied to {username}'s  with {phrase}")
        except tw.TweepyException as tweep_error:
            print(f"Twitter API Error: {str(tweep_error)}")
        except StopIteration:
            break

    # For the last four labels (Reply, Favorite, Retweet and Follow),
    # we need to check to see if the input from the user is “yes” or “no”
    # in order to run that given function or not.
    if favorite and retweet == "yes":
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

    if reply == "yes":
        for tweet in tw.Cursor(api.search_tweets, search_term).items(number_of_tweets):
            try:
                tweet_id = tweet.user.id
                username = tweet.user.screen_name
                api.update_status(status=f"@{username} {phrase}", in_reply_to_status_id=tweet_id)
                print(f"Replied to {username}'s  with {phrase}")
            except tw.TweepyException as tweep_error:
                print(f"Twitter API Error: {str(tweep_error)}")
            except StopIteration:
                break



# packing labels
# so that they show up and then call the root function in a loop
# so that it remains on the screen and doesn’t immediately close.
label_1.pack()
E1.pack()
label_2.pack()
E2.pack()
label_3.pack()
E3.pack()
label_4.pack()
E4.pack()
label_5.pack()
E5.pack()
label_6.pack()
E6.pack()
label_7.pack()
E7.pack()

# Add submit button & packing
submit_button = tk.Button(root, text="Submit", command=bot_function)
submit_button.pack()

root.mainloop()

# store user input in labels using .get() function
# then call function getE1() in bot_function() and
# store the input into a variable
def get_e1():
    return E1.get()
def get_e2():
    return E2.get()
def get_e3():
    return E3.get()
def get_e4():
    return E4.get()
def get_e5():
    return E5.get()
def get_e6():
    return E6.get()
def get_e7():
    return E7.get()