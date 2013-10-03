from collections import deque
import pygraphviz as pgv;

G = pgv.AGraph("karate.dot")

old_degree = 1

# Higher values of alpha result in smaller communities.
# If Alpha > degree of starting vertex, the algorithm fails.
# Lower values of alpha result in larger communities.
alpha = float(4)
v = G.get_node("3") # starting vertex.

community = []
shell = [v]
next_shell = []
depth = 0
total_emerging_degree = 0
to_append_to_community = []

while len(shell) > 0:

	emerging_degree = 0
	j = shell.pop(0)
	to_append_to_community.append(j)	
	neighbors = G.neighbors(j)

# remove community members (and members-to-be) from neighbors.
	for member in neighbors:
		if to_append_to_community.count (member) > 0:
			neighbors.remove (member)
		if community.count (member) > 0:
			neighbors.remove(member)
	external_vertices = neighbors


# Current shell members can be neighbors, as long as we haven't visited them.
# Current shell members shouldn't be added to the next shell.

# Add members not in this shell to the next shell.
	for member in external_vertices:
		if shell.count(member) == 0 and to_append_to_community.count(member) == 0 and community.count(member) == 0:
			next_shell.append(member)


# Append all of the outward facing vertices
	emerging_degree = len(external_vertices)
	total_emerging_degree += emerging_degree
	if len(shell) == 0:
		print depth, " completed."
		depth = depth +1
		shell = next_shell
		next_shell = []
		delta_degree = float(total_emerging_degree)/float(old_degree)
		if delta_degree < alpha:
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


print len (community), " nodes in community, of ", len (G.get_nodes)
print G.subgraph(community)
