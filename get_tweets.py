import os
import time
import tweepy
import pandas as pd
from dotenv import load_dotenv

# Set API Keys required to access Twitter

load_dotenv()
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

#! Authenticate Tweepy using saved keys

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

#* Create directory to save tweets

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_PATH = os.path.dirname(BASE_DIR)
tweets_file = os.path.join(BASE_DIR, "tweets", "tweets.csv")

# ToDO : Create folder & file if not exist

#* Set Variables
username = '' # user "@username" e.g "LibranTechie" - My handle
count = 50;

#* Get tweets
def get_tweets(username, count):
    try:
        tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)
        tweet_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets] # List comprehension.
        tweets_df = pd.DataFrame(tweet_list) #Dump the data into a pandas dataframe
        tweets_df.to_csv(tweets_file, header=True) #Send the data into a CSV file
        return tweets_df
    except BaseException as e:
        print(f"Failed on status, {str(e)}")
        time.sleep(3)


