#!/usr/bin/python
import sys
from directed_hypergraph import *

def main(argv):
    # Specify the name of the file containing the nodes and edges
    inPrefix = argv[0]
    outPrefix = argv[1]

    createNodeFile(inPrefix, outPrefix,argv[2],argv[3],delim=';',sep='\t')
    createEdgeFile(inPrefix, outPrefix)

def createNodeFile(in_prefix, out_prefix,pz=0.75,pen=10, delim=';', sep='\t'):

    inFileName = "/Users/bpotter/Desktop/Thesis/reactomeData/reactomeHypergraphs/"+in_prefix+"-hypernodes.txt"
    inNodes = open(inFileName, 'r')
    outFileName = "../hypergraphs/"+out_prefix+"-nodes.txt"
    outNodes = open(outFileName, 'w')
    outNodes.write("name;prize;penalty\n")

    # Skip the header line
    inNodes.readline()

    line_number = 2
    for line in inNodes.readlines():
        line = line.strip()
        # Skip empty lines
        if not line:
            continue

        words = line.split(sep)
        if not (len(words) == 2):
            raise \
                IOError("Line {} ".format(line_number) + "contains {} ".format(len(words)) + "columns -- must contain only 2.")

        # Change this to 1 to use nodes instead of hypernodes.
        node_ID = str(words[0])

        #
        # Add code to separate nodes
        #

        # Default prizes and penalties
        defPrize = pz
        defPenalty = pen


        outNodes.write(node_ID+";"+str(defPrize)+";"+str(defPenalty)+"\n")

        line_number += 1

    inNodes.close()
    outNodes.close()

def createEdgeFile(in_prefix, out_prefix, delim=';', sep='\t'):

    inFileName = "/Users/bpotter/Desktop/Thesis/reactomeData/reactomeHypergraphs/"+in_prefix+"-hyperedges.txt"
    inEdges = open(inFileName, 'r')
    outFileName = "../hypergraphs/"+out_prefix+"-edges.txt"
    outEdges = open(outFileName, 'w')
    outEdges.write("tail;head;cost\n")

    # Skip the header line
    inEdges.readline()

    line_number = 2
    for line in inEdges.readlines():
        line = line.strip()
        # Skip empty lines
        if not line:
            continue

        words = line.split(sep)
        if not (len(words) == 5):
            raise \
                IOError("Line {} ".format(line_number) + "contains {} ".format(len(words)) + "columns -- must contain only 5.")

        name = words[4]
        tail = words[0].split(delim)
        if tail[0] == "None":
            tail = []
        head = words[1].split(delim)
        posReg = words[2].split(delim)
        if posReg[0] != "None":
            tail.extend(posReg)
        if len(tail) == 0 or len(head) == 0:
            print("Skipping")
            continue


        # Default cost
        defCost = 1

        # Begin printing to edge file
        #outEdges.write(name+";")

        isFirst = True
        for node in tail:
            if isFirst:
                outEdges.write(node)
                isFirst = False
            else:
                outEdges.write(","+node)

        outEdges.write(";")

        isFirst = True
        for node in head:
            if isFirst:
                outEdges.write(node)
                isFirst = False
            else:
                outEdges.write(","+node)

        outEdges.write(";"+str(defCost)+"\n")

        line_number += 1

    inEdges.close()
    outEdges.close()

if __name__ == "__main__":
    main(sys.argv[1:])
