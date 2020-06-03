import os
import tweepy


# Authentication
consumer_key = os.getenv("CONSUMER_API_KEY")
consumer_secret = os.getenv("CONSUMER_API_SECRET_KEY")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


class TwitterApi:
    # Authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Update the status
    def send_tweet(self, message):
        self.api.update_status(status=message)
    
    # Display the timeline
    def display_timeline(self):
        timeline = self.api.home_timeline()
        for tweet in timeline:
            print(f"{tweet.user.screen_name}: {tweet.text}")    


client = TwitterApi()