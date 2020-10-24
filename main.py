import os
import tweepy
import pandas as pd
from dotenv import load_dotenv

# Set API Keys required to access Twitter

load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_secret = os.getenv('access_secret')

