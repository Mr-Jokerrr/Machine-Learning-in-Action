import regTrees
from numpy import *
import matplotlib.pyplot as plt

myDat = regTrees.loadDataSet('ex2.txt')
myMat = mat(myDat)
myTree = regTrees.createTree(myMat,ops=(0,1))


myDataTest = regTrees.loadDataSet('ex2test.txt')
myMatTest = mat(myDataTest)
r = regTrees.prune(myTree,myMatTest)

print(r)