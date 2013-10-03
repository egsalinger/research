import pygraphviz as pgv;
import sys, getopt
# Simple program to convert simple GML format graphs to DOT graphs
G = pgv.AGraph()

def main (argv):
 inputfile = ''
 outputfile = 'output.DOT'
 try:
	opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
 except getopt.GetoptError:
	print 'test.py -i <inputfile> [-o <outputfile>]'
	sys.exit(2)
 for opt, arg in opts:
	if opt == '-h':
		print 'test.py -i <inputfile> [-o <outputfile>]'
		sys.exit()
	elif opt in ("-i", "--ifile"):
		inputfile = arg
	elif opt in ("-o", "--ofile"):
		outputfile = arg
 print 'Input file is ', inputfile
 print 'Output file is ', outputfile


 with open (inputfile) as file:
	source = ""
	target = ""
	for line in file:
		words = line.split()
		if words[0] == "id":
			G.add_node (words[1])
		if words[0] == "source":
			source = words[1]
			target = ""
		if words[0] == "target" and source != "":
			target = words[1]
			G.add_edge(source, target)
			source = ""
			target = ""
	file.close()

 G.write (outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
		