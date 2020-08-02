from main_config import create_api, FOLLOW_FOR_FOLLOWER, FOLLOW, LIKE, REPLY_TO_MENTIONS, FAVANDRETWEET
import tweepy
import time


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                if LIKE:
                    tweet.favorite()
                    print(
                        f'Favoraited The Tweet from {tweet.user.screen_name}')
            except Exception as e:
                pass
        if not tweet.retweeted:
            try:
                tweet.retweet()
                print(f'Re-tweeted the Tweet of {tweet.user.screen_name}')
            except Exception as e:
                pass


def callTheFavandRetweet(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


def main():
    if FAVANDRETWEET:
        callTheFavandRetweet(
            ['100DaysOfCode', 'python', 'womanWhoCode', 'javascript'])


if __name__ == "__main__":
    main()
