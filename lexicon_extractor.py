
#!/usr/bin/python3
import os
import json

dir_path = '/Users/siddhant/dal/DWH/Assignment2/'
# dir_path = '/home/ubuntu/' on server

def split_tab(line):
  line_split = line.split("\t")
  return line_split

def extract_words(column):
  id = column[4].split(" ")
  words = [w.split("#")[0] for w in id]
  return words

def get_float(value):
  try:
    value = float(value)
    return value
  except ValueError:
    return float(0)

def extract_positive_score(column):
  return get_float(column[2])

def extract_negative_score(column):
  return get_float(column[3])

def extract_score(column):
  return 1 - (get_float(column[2]) + get_float(column[3]))

def extract_all_scores(file):
  try:
    os.remove(dir_path + 'dictionary2.json')
  except OSError:
    pass
  file = open(file)
  dictionary = {}
  for line in file:
    f = open(dir_path + "dictionary2.json", "a")
    if not line.startswith("#"):
      column = split_tab(line)
      words = extract_words(column)
      for word in words:
        dictionary[word] ={'neutral_score': extract_score(column),'positive_score': extract_positive_score(column),'negative_score': extract_negative_score(column)}
  dict = json.dumps(dictionary)
  f.write(dict)
  f.close()
