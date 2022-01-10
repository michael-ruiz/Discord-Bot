import tweepy

all_keys = open('keys.txt', 'r').read().splitlines()

api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

def send_tweet(message):
    api.update_status(message)

def update_profile_description(new_description):
    api.update_profile(desription=new_description)