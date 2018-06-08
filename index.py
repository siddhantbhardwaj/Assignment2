import tweets_extractor
import lexicon_extractor
import tweet_sentiment_transformer
import insert_tweets_elasticsearch
import os
import csv

dir_path = '/Users/siddhant/dal/DWH/Assignment2/'
# dir_path = '/home/ubuntu/' on server

with open(dir_path+"stopper.txt", 'r+') as file:
	open_file = csv.reader(file)
	for row in open_file:
		if(row[0] == "0"):
			lexicon_extractor.extract_all_scores(dir_path + 'SentiWordNet_3.0.0_20130122.txt')
			tweets_extractor.generate_tweets_csv()
			tweet_sentiment_transformer.transform_tweets()
			insert_tweets_elasticsearch.save_tweets_to_elasticsearch()
			file.seek(0)
			file.truncate()
			file.write("1")