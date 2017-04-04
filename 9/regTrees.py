'''
Tree-Based Regression Methods
Chapter 9, Machine Learning in Action
'''
from numpy import *
#	common functions
def regLeaf(dataSet):
    return mean(dataSet[:,-1])	#	return the mean of the last colume of dataSet
	
def regErr(dataSet):
    return var(dataSet[:,-1]) * shape(dataSet)[0]	#	reutrn the whole variance
	
def loadDataSet(fileName):	#	read from the data file and return a matrix of float data
	dataMat  = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = list(map(float, curLine))
		dataMat.append(fltLine)
	return dataMat

def binSplitDataSet(dataSet, feature, value):	#	divide dataSet into two subset depending on feature's value
	mat0 = dataSet[nonzero(dataSet[:,feature] > value)[0], :]
	mat1 = dataSet[nonzero(dataSet[:,feature] <= value)[0], :]
	return mat0, mat1

def createTree(dataSet,leafType=regLeaf, errType=regErr, ops=(1,4)):
	feat, val = chooseBestSplit(dataSet, leafType, errType, ops)	#	get the best feature and value to split
	if feat == None:	#	the best is not to split the tree, return mean value of this subset
		return val
	retTree = {}
	retTree['spInd'] = feat
	retTree['spVal'] = val
	lSet, rSet = binSplitDataSet(dataSet, feat, val)	#	split into two subsets
	retTree['left'] = createTree(lSet, leafType, errType, ops)	#	use recursion to create subtrees
	retTree['right'] = createTree(rSet, leafType, errType, ops)
	return retTree

#	CART
def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
	tolS = ops[0]	#	the decrease of variance must be bigger than tolS or the split will not be implemented
	tolN = ops[1]	#	the number of sample must be bigger than tolN or the split will not be implemented
	if len(set(dataSet[:,-1].T.tolist()[0])) == 1:	#	if all ys are of the same value then return, notice function set()
		return None, leafType(dataSet)
	m,n = shape(dataSet)
	S = errType(dataSet)
	bestS = float("inf")
	bestIndex = 0
	bestValue = 0
	for featIndex in range(n-1):	#	go through every feature, notice that n represent the coulume of y
		for splitVal in set((dataSet[:,featIndex].T.tolist())[0]): 	#	go through every colume
			mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
			if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
				continue
			newS = errType(mat0) + errType(mat1)
			if newS < bestS:
				bestIndex = featIndex
				bestValue = splitVal
				bestS = newS
	if (S - bestS) < tolS:	#	if the decrease is too small, undo the split and return
		return None, leafType(dataSet)
	mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
	if(shape(mat0)[0] < tolN):
		return None, leafType(dataSet)
	return bestIndex, bestValue

#	Post-Pruning
def isTree(obj):
	return (type(obj).__name__ == 'dict')

def getMean(tree):	#	get mean value of the whole tree
	if isTree(tree['right']):
		tree['right'] = getMean(tree['right'])
	if isTree(tree['left']):
		tree['left'] = getMean(tree['left'])
	return (tree['left'] + tree['right'])/2

def prune(tree, testData):	#	use training tree data to split test data
	if shape(testData)[0] == 0:	#	if there's no testData
		return getMean(tree)
	if (isTree(tree['right']) or isTree(tree['left'])):	#	if one of the two subtree exist, split it
		lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])	#	use the best value and featIndex of training data to split test data
	if isTree(tree['left']):	#	if the left subtree exist, use recursion to split it
		tree['left'] = prune(tree['left'], lSet)
	if isTree(tree['right']):
		tree['right'] = prune(tree['right'], lSet)
	if (not isTree(tree['left'])) and (not isTree(tree['right'])):	#	when reaching leaf nodes
		lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
		errorNoMerge = sum(power(lSet[:, -1] - tree['left'], 2)) + sum(power(rSet[:, -1] - tree['right'], 2))
		treeMean = (tree['left'] + tree['right'])/2.0
		errorMerge = sum(power(testData[:,-1] - treeMean, 2))	#	the error when do merge
		if errorMerge < errorNoMerge:	#	if errorMerge<errorNoMerge, merge the to data together and get the mean of them
			print("merging")
			return treeMean
		else:
			return tree
	else:
		return tree
		
