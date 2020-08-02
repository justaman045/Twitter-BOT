# Importing The Libraries
import os
try:
    import tweepy
    from time import sleep
except ModuleNotFoundError as e:
    os.system('pip install tweepy')

# API Keys for the Bot
consumer_key = '8wQX4CL66mRy64tgLj74ZGsfB'
consumer_secret = 'EkWrNBn4vBxQSEE7HPsNYhMN2ep03htoWgmQXpKwh6WnKd9usK'
access_token = '1284818562549456897-KQJALXqkkTdXLQGLX1bFhphnDNZMqB'
access_token_secret = 'vdCsHt56524AytYIKgXLI8tfgLf2GDCmxUifdKYx5IY3a'

# Getting the Hashtags
QUERY = '#100DaysOfCode,#python'

# Settings for the BOT
LIKE = True
TWEET = True

# Authentication for the BOT
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Printing The Settings
print("Twitter bot which Re-Tweets and Likes The Tweet")
print("Bot Settings")
print("Like Tweets :", LIKE)
print('Re-Tweet :', TWEET)

# Making the Main Tweet and Retweet


# def makeTheTweet(hashtag):
# print(hashtag)
for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        if TWEET == True:
            print(
                f'Re-Tweeting The Tweet By {tweet.user.screen_name} and the Tweet Id = {tweet.id}')
            tweet.retweet()
        if LIKE:
            print(
                f'Favoraiting The Tweet By {tweet.user.screen_name} and the Tweet Id = {tweet.id}')
            tweet.favorite()
    except tweepy.TweepError as e:
        pass


# hashtags = QUERY.split(',')
# for i in hashtags:
#     makeTheTweet(i)

# api.update_status('First Tweet Via Python')
