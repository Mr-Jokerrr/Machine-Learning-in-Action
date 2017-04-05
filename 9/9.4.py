import regTrees
from numpy import *
import matplotlib.pyplot as plt

myMat = mat(regTrees.loadDataSet('exp2.txt'))
r = regTrees.createTree(myMat, regTrees.modelLeaf, regTrees.modelErr, (1,10))
print (r)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(myMat[:,0].flatten()[0],myMat[:,-1].flatten()[0], color = 'g', s = 15)

x1 = myMat[nonzero(myMat[:,0] < 0.285477)[0],0]
x2 = myMat[nonzero(myMat[:,0] >= 0.285477)[0],0]
ax.plot(x1, 3.468 + x1 * 1.1852, 'r')
ax.plot(x2, 0.0016985 + x2 * 11.96477, 'r')
plt.show()
