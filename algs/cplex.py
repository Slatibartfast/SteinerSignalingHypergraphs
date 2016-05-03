#!/usr/bin/python
import sys
import timeit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import subprocess

def main(argv):

    defPrizes = [2.5]
    defPenalty = [7.5]

    hyperedges = []
    nodes = []

    for i in range(len(defPrizes)):
        it1 = []
        it2 = []
        for j in range(len(defPenalty)):
            it1.append(0)
            it2.append(0)
        hyperedges.append(it1)
        nodes.append(it2)

    #defPrizes = [0,1]
    #defPenalty = [0,1]

    #hyperedges = [[0,0],[0,0]]
    #nodes = [[0,0],[0,0]]

    names = []

    count = 10000

    for i in range(len(defPrizes)):
        for j in range(len(defPenalty)):

            name = "outputFiles/Hh_DC_"+str(count)+".sol"
            names.append(name)

            subprocess.call(["python3 build_input_files.py Signaling-by-Hedgehog Signaling-by-Hedgehog "+str(defPrizes[i])+" "+str(defPenalty[j])],shell=True)

            subprocess.call(["python3 build_lp.py Signaling-by-Hedgehog"],shell=True)

            cplex()

            subprocess.call(["mv outputFiles/TEST.sol "+name],shell=True)

            proc = subprocess.Popen(["grep hyperedge.*value=.1 "+name+" | wc -l"], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            e = out
            print("\ne",e)
            hyperedges[i][j] = int(e)

            subprocess.call(["grep -v To "+name+" > outputFiles/grepv.txt"],shell=True)
            proc = subprocess.check_output(["grep Protein.*x.*value=.1 outputFiles/grepv.txt | wc -l"], shell=True)
            #(out, err) = proc.communicate()
            p = int(out)
            print("\np",p)

            proc = subprocess.Popen(["grep Complex.*x.*value=.1 outputFiles/grepv.txt | wc -l"], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            c = int(out)
            print("\nc",c)

            proc = subprocess.Popen(["grep SmallMolecule.*x.*value=.1 outputFiles/grepv.txt | wc -l"], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            s = int(out)
            print("\ns",s)

            n = c + s + p
            print("n",n)
            nodes[i][j] = n

            count += 1

            print("\n")
            print("H:",hyperedges)
            print("N:",nodes)

    subprocess.call(["rm *.png"],shell=True)

    makeHeatmap(hyperedges,defPrizes,defPenalty,"Hh_hyperedges.png","Blues","Hyperedge Overlap")
    makeHeatmap(nodes,defPrizes,defPenalty,"Hh_nodes.png","Reds","Node Overlap")

    return

def cplex():
    subprocess.call(["cplex < mycplexcommands"],shell=True)

def makeHeatmap(matrix,clabel,rlabel,filename,color,title):
    column_labels = clabel
    row_labels = rlabel
    data = np.array(matrix)
    fig, ax = plt.subplots()
    if color[0] == "B":
        heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
    else:
        heatmap = ax.pcolor(data, cmap=plt.cm.Reds)

    ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)

    #ax.invert_yaxis()
    #ax.xaxis.tick_top()


    ax.set_xticklabels(row_labels, minor=False)
    ax.set_yticklabels(column_labels, minor=False)
    ax.set_xlabel('Penalties')
    ax.set_ylabel('Prizes')
    ax.set_title(title)

    minimum = matrix[0][0]
    maximum = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

    middle = (minimum + maximum) / 2

    cbar = plt.colorbar(heatmap)
    #cbar.ax.set_yticklabels([str(minimum), str(middle), str(maximum)])
    #cbar.set_label('Times Present in Solution', rotation=270)
    plt.tight_layout()
    plt.savefig(filename)

    return

if __name__ == "__main__":
    main(sys.argv)
