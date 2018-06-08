
#Assignment 2 Steps

1. python3 cron.py

2. This will generate the csv files and one json file required for sentiment analysis and upload the data onto Elasticsearch.

Note:

1. Make sure that stopper.txt has text 0 before running the cron task mentioned above. This is to ensure that cron job runs only once.

2. Change the `dir_path` variable name to absolute path of the directory of the assignment.

3. If to import the data on elasticsearch, please change the file insert_tweets_elasticsearch.py 
connections.create_connection(hosts=['ec2-18-188-194-190.us-east-2.compute.amazonaws.com:9200'])

4. You may use your own connection as well.

Ayman Mohatarem 
B00787866

Siddhant Bhardwaj
B00779682

CSCI 5408
