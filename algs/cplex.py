#!/usr/bin/python
import sys
import timeit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from subprocess import call

def main(argv):

    defPrizes = [0,0.75,1,10,100]
    defPenalty = [0,1,10,100]

    hyperedges = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    nodes = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    names = []

    count = 0

    for i in range(len(defPrizes)):
        for j in range(len(defPenalty)):

            name = "Hh_"+str(count)+".sol"
            names.append(name)

            call(["python3 build_input_files.py Signaling-by-Hedgehog Signaling-by-Hedgehog "+str(defPrizes[i])+" "+str(defPenalty[j])],shell=True)

            call(["python3 build_lp.py Signaling-by-Hedgehog"],shell=True)

            cplex()

            call(["mv TEST.sol "+name],shell=True)

            e = call(["grep hyperedge.*value=\"1\" "+name+" | wc -l"],shell=True)
            hyperedges[i][j] = int(e)

            call(["grep -v To "+name+" > grepv.txt"],shell=True)
            p = int(call(["grep Protein.*value=\"1\" grepv.txt | wc -l"],shell=True))
            c = int(call(["grep Complex.*value=\"1\" grepv.txt | wc -l"],shell=True))
            s = int(call(["grep SmallMolecule.*value=\"1\" grepv.txt | wc -l"],shell=True))

            n = p + c + s
            nodes[i][j] = n

            count += 1

    print("H:",hyperedges)
    print("N:",nodes)

    makeHeatmap(hyperedges,defPrizes,defPenalty,"Hh_hyperedges.png")
    makeHeatmap(nodes,defPrizes,defPenalty,"Hh_nodes.png")

    return

def cplex():
    call(["cplex < mycplexcommands"],shell=True)

def makeHeatmap(matrix,clabel,rlabel,filename):
    column_labels = clabel
    row_labels = rlabel
    data = np.array(matrix)
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)

    ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    #ax.set__xticklabels(row_labels, minor=False)
    #ax.set__yticklabels(column_labels, minor=False)
    ax.set_xlabel('Penalties')
    ax.set_ylabel('Prizes')

    plt.savefig(filename)

    return

if __name__ == "__main__":
    main(sys.argv)
