#!/bin/bash
from crontab import CronTab
import os

cron = CronTab(user=True)

python_path = '/Users/siddhant/anaconda3/bin/python3'
dir_path = '/Users/siddhant/dal/DWH/Assignment2/'

# ON SERVER use the following python path
# python_path = '/usr/bin/python3'
# dir_path = '/home/ubuntu/'
command = '%sindex.py' % (python_path + ' ' + dir_path)

job = cron.new(command= command, comment='This should be rendered as comment when command is performed')
job.minute.every(1)

cron.write()
print("Job created")