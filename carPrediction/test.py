import dataProcessing
from numpy import *
import regTrees

trainDataSet = dataProcessing.loadData('datasets\\finalDataSet.csv')
testDataSet = dataProcessing.loadData('datasets\\finalDataSet2.csv')

for line in trainDataSet:
	del line[-1]
trainDataSet = mat(array(trainDataSet).astype(float))
trainDataSet[:, 0] = trainDataSet[:, 0]-20160000
for line in testDataSet:
	del line[-1]
testDataSet = mat(array(testDataSet).astype(float))
testDataSet[:, 0] = testDataSet[:, 0]-20170000

'''
regression tree
'''
print("step1, please wait...")
mytree1 = regTrees.createTree(trainDataSet[1:, :], ops=(0,10))
yHat1 = regTrees.createForeCast(mytree1, testDataSet[1:, :shape(testDataSet)[1]-1])

myResult1 = corrcoef(yHat1,testDataSet[1:, -1],rowvar = 0)[0, 1]
print("finished!")
print(myResult1)

'''
model tree
'''
print("step2, please wait...")
myTree2 = regTrees.createTree(trainDataSet[1:, :], regTrees.modelLeaf, regTrees.modelErr, ops=(1,12000))
yHat2 = regTrees.createForeCast(myTree2, testDataSet[1:, :shape(testDataSet)[1]-1], regTrees.modelTreeEval)

myResult2 = corrcoef(yHat2,testDataSet[1:, -1],rowvar = 0)[0, 1]
print("finished!")
print(myResult2)
