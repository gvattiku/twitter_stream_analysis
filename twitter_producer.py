import pickle
import requests
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

producer = KafkaProducer(bootstrap_servers="localhost:9092")

topic_name = ""

config = pickle.load("config.p", "rb")

class twitterAuth():

    def authenticateTwitterApp(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

class TwitterStreamer():

    def __init__(self):
        self.twitterAuth = twitterAuth()

    def stream_tweets(self):
        while True:
            listener = ListenerTS()
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            stream.filter(track = ["Apple"], stall_warnings=True, languages= ["en"])

class ListenerTS():

    def on_data(self, raw_data):
        producer.send(topic_name, str.encode(raw_data))
        return True

if __name__ = "__main__":
    TS = TwitterStreamer()
    TS.stream_tweets()