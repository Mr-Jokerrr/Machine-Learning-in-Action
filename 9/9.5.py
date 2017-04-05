import regTrees
from numpy import *
import matplotlib.pyplot as plt
import sys

def QuickSort(X, Y1, Y2, firstIndex, lastIndex):
	if firstIndex<lastIndex:
		divIndex=Partition(X, Y1, Y2, firstIndex, lastIndex)
		QuickSort(X, Y1, Y2, firstIndex, divIndex)       
		QuickSort(X, Y1, Y2, divIndex+1, lastIndex)
	else:
		return
def Partition(arr1, arr2, arr3,low,high):
	key1 = arr1[low]
	key2 = arr2[low]
	key3 = arr3[low]
	while low<high:
		while low < high and arr1[high] >= key1:
			high -= 1
		while low < high and arr1[high] < key1:
			arr1[low] = arr1[high]
			arr2[low] = arr2[high]
			arr3[low] = arr3[high]
			low += 1
			arr1[high] = arr1[low]
			arr2[high] = arr2[low]
			arr3[high] = arr3[low]
	arr1[low] = key1
	arr2[low] = key2
	arr3[low] = key3
	return low

trainMat = mat(regTrees.loadDataSet('bikeSpeedVsIq_train.txt'))
testMat = mat(regTrees.loadDataSet('bikeSpeedVsIq_test.txt'))

myTree1 = regTrees.createTree(trainMat, ops=(1,20))
yHat1 = regTrees.createForeCast(myTree1, testMat[:,0])
r1 = corrcoef(yHat1, testMat[:,1], rowvar=0)[0,1]
#print (r1)

myTree2 = regTrees.createTree(trainMat, regTrees.modelLeaf, regTrees.modelErr, ops=(1,20))
yHat2 = regTrees.createForeCast(myTree2, testMat[:,0], regTrees.modelTreeEval)
r2 = corrcoef(yHat2, testMat[:,1], rowvar=0)[0,1]
#print(r2)

fig = plt.figure()
ax = fig.add_subplot(121)

X = testMat[:,0]
Y = testMat[:,-1]

#savetxt("1.txt", yHat2, fmt="%f")
	
X_copy = X.copy()
Y1_copy = yHat1.copy()
Y2_copy = yHat2.copy()

QuickSort(X_copy, Y1_copy, Y2_copy, 0, len(testMat[:,0])-1)	#	QuickSort

ax.scatter(X.flatten()[0], Y.flatten()[0], color = 'c', s = 10)
ax.set_title("regresion tree")
ax.plot(X_copy, Y1_copy, 'r')
bx = fig.add_subplot(122)
bx.scatter(X.flatten()[0], Y.flatten()[0], color = 'c', s = 10)
bx.set_title("model tree")
bx.plot(X_copy, Y2_copy, 'm')
plt.show()

