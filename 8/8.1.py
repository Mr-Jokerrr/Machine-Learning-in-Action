import regression
from numpy import *
import matplotlib.pyplot as plt
xArr,yArr = regression.loadDataSet('ex0.txt')
ws=regression.standRegres(xArr,yArr)

xMat = mat(xArr)
yMat = mat(yArr)
yHat1 = xMat*ws

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
xCopy = xMat.copy()
xCopy.sort(0)
yHat2 = xCopy*ws
ax.plot(xCopy[:,1],yHat2)
corr = corrcoef(yHat1.T,yMat)
print(corr)
plt.show()