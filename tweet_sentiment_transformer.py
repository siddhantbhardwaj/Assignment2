#!/usr/bin/python3

import csv
import time
import json

dir_path = '/Users/siddhant/dal/DWH/Assignment2/'
# dir_path = '/home/ubuntu/' on server

def neutral_score(positive, negative):
  return 1 - (positive + negative)

def maximum_sentiment(positive, negative, neutral, number_of_words):
  positive = positive/number_of_words
  negative = negative/number_of_words
  neutral = neutral/number_of_words
  max = positive
  type = 'positive'
  if negative > max:
    max = negative
    type = 'negative'
  if neutral > max:
    max = neutral
    type = 'neutral'

  return  [type, max]


def retrive_sentiment(tweet, lexicon_data):
  positive = 0
  negative = 0
  neutral = 0
  number_of_words = 0
  for word in tweet[3].split(" "):
    tweet_word = lexicon_data.get(word.lower())
    if tweet_word is not None:
      positive = positive + tweet_word["positive_score"]
      negative = negative + tweet_word["negative_score"]
      neutral = neutral + tweet_word["neutral_score"]
      number_of_words = number_of_words + 1

  if positive == 0 and negative == 0 and  neutral == 0:
    return [None, None]

  type = maximum_sentiment(positive, negative, neutral, number_of_words)
  return [type[0], type[1]]


def transform_tweets():
  lexicon = open(dir_path + "dictionary2.json")
  lexicon = lexicon.read()
  lexicon_data = json.loads(lexicon)
  with open (dir_path + 'transformedTweets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['tweet', 'sentiment', 'sentiment_score'])
    with open(dir_path + 'tweets.csv', 'r') as tweets:
      csvtweets = csv.reader(tweets)
      for tweet in csvtweets:
        sentiment = retrive_sentiment(tweet, lexicon_data)
        if sentiment[0] is not None:
          writer.writerow([tweet[3] , sentiment[0], sentiment[1]])
