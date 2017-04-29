#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:41:19 2017


"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "142980981-4f95Lx897pPu9TWV3gsM8OBpxopbd93e8Jayjjox"
access_token_secret = "skfsV7rREgguYo7DYLZQYUDwadxTwIudLvSCt3rd6gnBA"
consumer_key = "bpdsWVZ0KrA3Ae3yu6Te0yicr"
consumer_secret = "74nbXsTkHUnEN75CI3LytMwd2aAABpzqH22boNmtJBHva5RN4H"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['donald trump', 'donaldtrump', 'trump'])