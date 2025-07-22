import os
from dotenv import load_dotenv
import tweepy as tw
import tkinter as tk

# Load environment variables from .env file
load_dotenv()

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Use Client for Twitter API v2
client = tw.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Check if program is working
try:
    me = client.get_me()
    print(f"Connected as: {me.data.name}")
except tw.TweepyException as e:
    print(f"Authentication Error: {e}")
except Exception as e:
    print(f"Error: {e}")

def bot_function():
    try:
        # Get inputs
        search = E1.get()
        number_of_tweets = int(E2.get())
        response = E3.get()
        reply = E4.get()
        favorite = E5.get()
        retweet = E6.get()
        follow = E7.get()

        # Search tweets (API v2)
        tweets = client.search_recent_tweets(
            query=search,
            max_results=min(number_of_tweets, 100)  # API v2 has a limit of 100
        )

        if tweets.data:
            for tweet in tweets.data:
                try:
                    if favorite.lower() == "yes":
                        client.like(tweet.id)
                        print(f"Liked tweet {tweet.id}")

                    if retweet.lower() == "yes":
                        client.retweet(tweet.id)
                        print(f"Retweeted tweet {tweet.id}")

                    if reply.lower() == "yes":
                        client.create_tweet(
                            text=response,
                            in_reply_to_tweet_id=tweet.id
                        )
                        print(f"Replied to tweet {tweet.id}")

                except tw.TweepyException as e:
                    print(f"Error processing tweet {tweet.id}: {e}")

    except tw.TweepyException as e:
        print(f"Twitter API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Create GUI
root = tk.Tk()
root.title("Twitter Bot")

# Labels and Entries
labels_entries = [
    ("Search", "E1"),
    ("Number of Tweets", "E2"),
    ("Response", "E3"),
    ("Reply (yes/no)", "E4"),
    ("Favorite (yes/no)", "E5"),
    ("Retweet (yes/no)", "E6"),
    ("Follow (yes/no)", "E7")
]

for label_text, entry_name in labels_entries:
    label = tk.Label(root, text=label_text)
    label.pack()
    entry = tk.Entry(root, bd=5)
    entry.pack()
    globals()[entry_name] = entry

submit_button = tk.Button(root, text="Submit", command=bot_function)
submit_button.pack()

root.mainloop()