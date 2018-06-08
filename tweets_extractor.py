#!/usr/bin/python3

import tweepy
import time
import json
import csv
import os

consumer_key = "zpMshFowGfpokKEZ4XiCbHKw5"
consumer_secret = "q3lTALK0NC7HBLBtIB7etncybWEPs7AYhNvW6SqGiqZ9aL7byc"
access_key = "1000023501812662273-Tkxup9gMue7t7fPFTHfjAyA39q8ass"
access_secret = "LlrQShY0eiQBXnr7ElyR3EehY8FBa5nYbRfvtvCBsTU59"
dir_path = '/Users/siddhant/dal/DWH/Assignment2/'
# dir_path = '/home/ubuntu/' on server

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_tweets(query):
  api = tweepy.API(auth)
  try:
     tweets = api.search(query, count=1000)
  except tweepy.error.TweepError as e:
     tweets = json.loads(e.response.text)
  
  return tweets


def generate_tweets_csv():
  tw = get_tweets("#realDonaldTrump")
  queries = ["#HanSolo", "\"Nova Scotia\"","@Windows","#realDonaldTrump"]

  with open (dir_path + 'tweets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id','user','created_at','text'])
    for query in queries:
      t = get_tweets(query)
      for tweet in t:
        writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('utf-8').strip()])
