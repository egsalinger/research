import sys
import simplejson
import pygraphviz as pgv
#import codecs
#from collections import OrderedDict

tweeters = []
tweeter_info = dict()
															
def parse_tweets ():
 counter = 0
   	      
 with open  ("data", "r") as myfile:
  for line in myfile.readlines():
	counter = counter+1
	tweet = simplejson.loads(line)
	doc = tweet["doc"]
        user=doc["from_user"]
	if not user in tweeter_info:
		tweeters.append(user)
	if user in tweeter_info:
		tweeter_info [user] = tweeter_info[user] + 1
	else:
		tweeter_info [user] = 1
	if counter%100000 == 0:
		print counter
  G = pgv.AGraph("MERGED.dot")
  for tweeter in tweeters:
	print "Username " + tweeter
	output = ""
	for predecessor in G.predecessors(tweeter):
		output +=  predecessor
		if predecessor in tweeter_info:
			i = tweeter_info.get (predecessor, -1)
			output += ":"+ str(i)
		output += " "
	print output;

def main():
	parse_tweets ()

if __name__ == '__main__':
    main()
