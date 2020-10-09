from DecisionTree import DecisionTree
import DataGeneration as dg
import numpy as np
import random as rd
import math

def informationContent(data):
    p0 = data.count(0)/len(data)
    p1 = data.count(1)/len(data)
    #print("P(Y = 0) : ", p0, ", P(Y = 1) : ", p1)
    if p0 == 0 or p1 == 0:
        return 0
    return (-1 * p0 * math.log2(p0)) - (p1 * math.log2(p1))

def informationContentX(data):
    icx = []
    for i in range(len(data[0][0])):
        #print("X", i+1, " : ")
        xi = [j[0][i] for j in data]
        #print(xi)
        p0 = xi.count(0)/len(xi)
        p1 = xi.count(1)/len(xi)
        #print("P(X = 0) : ", p0, ", P(X = 1) : ", p1)
        if p0 == 0:
            xi0 = 0
            xi1 = p1 * informationContent([j[1] for j in data if j[0][i] == 1])
        elif p1 == 0:
            xi0 = p0 * informationContent([j[1] for j in data if j[0][i] == 0])
            xi1 = 0
        else:
            xi0 = p0 * informationContent([j[1] for j in data if j[0][i] == 0])
            xi1 = p1 * informationContent([j[1] for j in data if j[0][i] == 1])
        icx.append(xi0 + xi1)
        #print(icx[i])
    return icx

def informationGain(data):
    features = [i[0] for i in data]
    #print("Features : ")
    #for f in features:
    #    print(f)
    #print("Y : ")
    y = [i[1] for i in data]
    #for i in y:
    #    print(i)
    hy = informationContent(y)
    #print("H(Y) : ", hy)
    hyx = informationContentX(data)
    #print("H(Y|X) : ")
    #for h in hyx:
    #    print(h)
    ig = [0 for i in features[0]]
    for i in range(len(features[0])):
        ig[i] = hy - hyx[i]
    #print("Information Gain : ")
    #for i in ig:
    #    print(i)
    return ig

def splitData(data, igmax):
    d0 = [i for i in data if i[0][igmax] == 0]
    d1 = [i for i in data if i[0][igmax] == 1]
    return [d0, d1]

def decisionTree(data):
    ig = informationGain(data)
    if ig.count(0) == len(ig):
        return None
    print(ig)
    ig = np.array(ig)
    igmaxindex = np.where(ig == max(ig))[0]
    igmax = rd.choice(igmaxindex)
    root = DecisionTree(val = igmax)
    datasplit = splitData(data, igmax)
    print(igmax)
    print("d0")
    for d in datasplit[0]:
        print(d)
    print("d1")
    for d in datasplit[1]:
        print(d)
    root.left = decisionTree(datasplit[0])
    if root.left == None:
        root.left = DecisionTree(val = float(datasplit[0][0][1]))
    root.right = decisionTree(datasplit[1])
    if root.right == None:
        root.right = DecisionTree(val = float(datasplit[1][0][1]))
    return root
    
data = dg.dataGeneration(4, 30)
print("Data : ")
for d in data:
    print(d)
tree = decisionTree(data)

print("BFS")
if tree:
    queue = [tree]

    while queue:
        temp_print = []
        temp_children = []
        while queue:
            curr = queue.pop(0)
            temp_print.append(curr.val)
            if curr.left:
                temp_children.append(curr.left)
            if curr.right:
                temp_children.append(curr.right)
        print(temp_print)
        queue = temp_children[:]

else:
    print(data[0][1])
    
