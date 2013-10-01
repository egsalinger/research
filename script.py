# Author: Eric Salinger
# e-mail: egs9108 (at) g.rit.edu
# Basic script that reads all of our twitter data and outputs, for each user, the number of tweets that the users friends have made.
# This is intended primarily as a learning exercise for picking python back up.
# You are certainly welcome to use this code however you like, and if you have a question, you are certainly welcome to e-mail me. I do not, however, guarantee that I will be able to provide you with an answer.


import sys
import simplejson
import pygraphviz as pgv

#List of people who are tweeters, because I wasn't sure how to deal with keysets
tweeters = []
#Key:	Tweeter
#Value:	#of tweets
tweeter_info = dict()

# Parses all tweets.
def parse_tweets ():
 # just so you know things haven't crashed. "data" is 400 mb.
 counter = 0

 with open  ("data", "r") as myfile:
#TODO: Replace this with a less memory intensive read.
  for line in myfile.readlines():
	counter = counter+1
# Parse data line by line and extricate the tweeter from the file.
	tweet = simplejson.loads(line)
	doc = tweet["doc"]
        user=doc["from_user"]
# Adds tweeter's info to map If they are in the map, add 1 to their value, if they are not in the map, put them in with value of 1.
	if not user in tweeter_info:
		tweeters.append(user)
	if user in tweeter_info:
		tweeter_info [user] = tweeter_info[user] + 1
	else:
		tweeter_info [user] = 1
	if counter%100000 == 0:
		print counter
  G = pgv.AGraph("MERGED.dot")
# Iterate through all of the tweeters.
  for tweeter in tweeters:
# print them
	print "Username " + tweeter
	output = ""
# and the number of tweets their friends have made, for each individual friend.
	for predecessor in G.predecessors(tweeter):
		output +=  predecessor
		if predecessor in tweeter_info:
			i = tweeter_info.get (predecessor, -1)
			output += ":"+ str(i)
		output += " "
	print output;

# Stuff we need to make program go.
def main():
	parse_tweets ()

if __name__ == '__main__':
    main()
