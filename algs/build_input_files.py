#!/usr/bin/python
import sys
from directed_hypergraph import *

def main(argv):
    # Specify the name of the file containing the nodes and edges
    inPrefix = input("What is the prefix of input files (without -hypernodes or -hyperedges)? ")
    outPrefix = input("What should the prefix of the output files be? ")

    createNodeFile(inPrefix, outPrefix)
    createEdgeFile(inPrefix, outPrefix)

def createNodeFile(in_prefix, out_prefix, delim=';', sep='\t'):

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
        defPrize = 1
        defPenalty = 5

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
        head = words[1].split(delim)
        posReg = words[2].split(delim)
        if posReg[0] != "None":
            tail.extend(posReg)

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
    main(sys.argv)
