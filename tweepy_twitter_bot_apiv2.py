import os
from dotenv import load_dotenv
import tweepy as tw
import tkinter as tk
from typing import Dict

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

class TwitterBot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Twitter Bot")
        self.entries: Dict[str, tk.Entry] = {}
        self.setup_gui()

    def setup_gui(self):
        # Labels and Entries
        labels_entries = [
            ("Search", "search"),
            ("Number of Tweets", "tweets_number"),
            ("Response", "response"),
            ("Reply (yes/no)", "reply"),
            ("Favorite (yes/no)", "favorite"),
            ("Retweet (yes/no)", "retweet"),
            ("Follow (yes/no)", "follow")
        ]

        for label_text, entry_key in labels_entries:
            label = tk.Label(self.root, text=label_text)
            label.pack()
            entry = tk.Entry(self.root, bd=5)
            entry.pack()
            self.entries[entry_key] = entry

        submit_button = tk.Button(self.root, text="Submit", command=self.bot_function)
        submit_button.pack()

    def bot_function(self):
        try:
            # Get inputs
            search = self.entries["search"].get()
            number_of_tweets = int(self.entries["tweets_number"].get())
            response = self.entries["response"].get()
            reply = self.entries["reply"].get()
            favorite = self.entries["favorite"].get()
            retweet = self.entries["retweet"].get()
            follow = self.entries["follow"].get()

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

                        if follow.lower() == "yes":
                            client.follow_user(tweet.author_id)
                            print(f"Followed user {tweet.author_id}")

                    except tw.TweepyException as tweep_error:
                        print(f"Error processing tweet {tweet.id}: {tweep_error}")

        except tw.TweepyException as tweep_error:
            print(f"Twitter API Error: {tweep_error}")
        except ValueError as val_error:
            print(f"Input Error: {val_error}")
        except Exception as general_error:
            print(f"Error: {general_error}")

    def run(self):
        # Check if program is working
        try:
            me = client.get_me()
            print(f"Connected as: {me.data.name}")
        except tw.TweepyException as auth_error:
            print(f"Authentication Error: {auth_error}")
            return

        self.root.mainloop()

if __name__ == "__main__":
    bot = TwitterBot()
    bot.run()