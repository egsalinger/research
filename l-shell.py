from collections import deque
import pygraphviz as pgv;

G = pgv.AGraph("karate.dot")

old_degree = 1

# Higher values of alpha result in smaller communities.
# If Alpha > degree of starting vertex, the algorithm fails.
# Lower values of alpha result in larger communities.
alpha = float(1.9)
v = G.get_node("24") # starting vertex.

# The detected community.
community = []
# The current shell we're examining (starts as the starting vertex).
shell = [v]
# the nodes in the next shell.
next_shell = []
depth = 0
total_emerging_degree = 0
# the nodes that will be appended to the community. This is basically the current shell.
to_append_to_community = []

while len(shell) > 0:

	emerging_degree = 0
	j = shell.pop(0)
	neighbors = []
# if you're neither in our community, nor going to be added to our community
	if to_append_to_community.count(j) == 0 and community.count(j) == 0:
# we should append you to the community, and get your neighbors for further processing.
		to_append_to_community.append(j)
		neighbors = G.neighbors(j)
#	else:
#		print "Popped ", j, " which was not supposed to be in the community."

# remove community members (and members-to-be) from neighbors.

# The total emerging degree is the sum of emerging degrees (defined as
# the number of vertices from the current shell to unvisited
# nodes).
	external_vertices = []
	
	for member in neighbors:
		if to_append_to_community.count (member) == 0 and community.count (member) == 0 and shell.count(member) == 0:
			external_vertices.append (member)
#			print "Appending ", member	

# Current shell members can be neighbors, as long as we haven't visited them.
# Current shell members shouldn't be added to the next shell.

# Add members not in this shell to the next shell. Note that external_vertices
# may have duplicate entries.
	for member in external_vertices:
		if next_shell.count(member) == 0:
#			print "appending ", member
			next_shell.append(member)
			
# Append all of the outward facing vertices
	emerging_degree = len(external_vertices)
	total_emerging_degree += emerging_degree

	if len(shell) == 0:
#		print depth, " completed."
#		print total_emerging_degree
#		print "next shell is: ",next_shell
		depth = depth +1
		shell = next_shell
		next_shell = []
		delta_degree = float(total_emerging_degree)/float(old_degree)
		if delta_degree < alpha:
			community = community + to_append_to_community
			op = str(total_emerging_degree)
			if len (op) < len(str(old_degree)):
				op = old_degree
			op = len (op) + 2
			output = ""
			for i in range (0,op):
				output += "-"

			print "Community around starting node detected."
			print  " " + str(total_emerging_degree)
			print output + " = ", delta_degree, " < ", alpha
			print " " + str(old_degree)
			break
# the old degree is the total emerging degree of the previous shell.
		old_degree = total_emerging_degree
# the new total emerging degree is 0
		total_emerging_degree = 0
# this stops adding edges that don't belong to the community to the community. In this example,
# we have two complete subgraphs ((a,b,c,d) and (1,2,3,4), respectively) that are connected. If we
# added directly to the current shell, we would detect community (1,2,3,4,a), which is clearly
# a mistake.
		
		community = community + to_append_to_community
		to_append_to_community = []
		if len(shell) == 0:
			print "Entire graph is a community."
			break
# If we haven't reached the point where this shell isn't a shell, 


print len (community), " nodes in community, of ", len (G.nodes())
print G.subgraph(community)
#print community
