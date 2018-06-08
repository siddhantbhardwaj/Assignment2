#!/usr/bin/python3

from elasticsearch_dsl import DocType, Float, Keyword, Text, connections
import csv

connections.create_connection(hosts=['ec2-18-188-194-190.us-east-2.compute.amazonaws.com:9200'])

dir_path = '/Users/siddhant/dal/DWH/Assignment2/'
# dir_path = '/home/ubuntu/' on server

def get_float(value):
  try:
    value = float(value)
    return value
  except ValueError:
    return float(0)

class Tweet(DocType):
  tweet = Text()
  sentiment = Keyword()
  sentiment_score = Float()

  class Meta:
    index = 'tweets'



def save_tweets_to_elasticsearch():
  Tweet.init(index="tweets")
  with open(dir_path+"transformedTweets.csv", 'r') as file:
    open_file = csv.reader(file)
    id_count = 0
    for row in open_file:
      new_tweet = Tweet(meta = {'id': id_count})
      new_tweet.tweet = row[0]
      new_tweet.sentiment = row[1]
      new_tweet.sentiment_score = get_float(row[2])
      new_tweet.save()
      new_tweet = Tweet.get(id = id_count)
      id_count = id_count +1
      print(row)

