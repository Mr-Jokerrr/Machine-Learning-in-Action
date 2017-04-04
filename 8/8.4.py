import regression
from numpy import *
import matplotlib.pyplot as plt
xArr,yArr = regression.loadDataSet('abalone.txt')
a=regression.stageWise(xArr,yArr,0.01,200)
print(a)