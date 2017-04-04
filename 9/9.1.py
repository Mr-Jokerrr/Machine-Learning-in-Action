import regTrees
from numpy import *
import matplotlib.pyplot as plt
testMat = mat(eye(4))
mat0,mat1 = regTrees.binSplitDataSet(testMat, 1, 0.5)
print(mat0)
print(mat1)