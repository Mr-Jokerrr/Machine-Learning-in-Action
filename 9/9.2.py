import regTrees
from numpy import *
import matplotlib.pyplot as plt

myDat1 = regTrees.loadDataSet('ex00.txt')
myMat1 = mat(myDat1)
r1 = regTrees.createTree(myMat1)
print(r1)
print()

myDat2 = regTrees.loadDataSet('ex0.txt')
myMat2 = mat(myDat2)
r2 = regTrees.createTree(myMat2)
print(r2)