# -*- coding:UTF-8 -*-
'''
data processing
updated on Sunday, April 16th, 2017
'''

import csv
import time
import datetime

#	function to load data(csv file)
def loadData(fileName):
	a = []
	with open(fileName, "r") as f:
		for data in f.readlines():
			if data:
				a.append(data.replace("\r\n","").split(","))
	return a

#	write inputData into a csv file named fileName
def writeData(inputData, fileName):
	with open(fileName, "w", encoding="utf-8") as f:
		for i in range(len(inputData)):
			for data in inputData[i]:
				if data:
					f.write(data)
					f.write(",")
			if i< len(inputData)-1:
				f.write("\n")
	return

#	combine the datas in fileName1 and fileName2 and return the combinedData
def combineData(fileName1, fileName2):
	a1 = []; a2 = []; combinedData = [];
	a1 = loadData(fileName1); a2 = loadData(fileName2)
	print("There are ",len(a1)-1," rows of data under processing")
	for i in range(len(a1)):
		combinedData.append(a1[i])
		combinedData[i][0], combinedData[i][1] =\
			combinedData[i][1], combinedData[i][0]	# make the data column on the first column
		combinedData[i][0] = datetime.datetime.strptime(combinedData[i][0], '%Y-%m-%d')\
			.strftime("%Y%m%d")	#	change the format of data,month,year
		for j in range(len(a2)):
			if time.strptime(a1[i][0], '%Y%m%d') == time.strptime(a2[j][0], '%Y-%m-%d'):
				combinedData[i].extend(a2[j][1:])
				break
		if i%1000==0:
			print(int(i/1000),"thousand data are already processed......")
	print("Processing done!")
	return combinedData

#	select the data between beginDate and endData, and return the validDataSet
def validDataSet(dataSet,beginDate,endDate):
	validDataSet = []
	for line in dataSet:
		if time.strptime(line[0], "%Y%m%d")>=time.strptime(beginDate, "%Y%m%d")\
			and time.strptime(line[0], "%Y%m%d")<=time.strptime(endDate, "%Y%m%d"):
			validDataSet.append(line)
	return validDataSet

def calcuDays(inputDate):
	t = time.strptime(inputDate, '%Y%m%d')
	year = t.tm_year
	month = t.tm_mon
	day = t.tm_mday
	date = datetime.date(year, month, day)
	outputDays = date.strftime('%j')
	return str(outputDays)

#	achieve switch case
def weatherDir(weather):
	switcher = {
		"暴雪":"1",
		"暴雨":"2",
		"大雪":"3",
		"大雨":"4",
		"中雪":"5",
		"中雨":"6",
		"小雪":"7",
		"小雨":"8",
		"雨夹雪":"9",
		"阵雨":"10",
		"晴":"11",
	}
	return switcher.get(weather, 00000000)

def airconDir(aircon):
	switcher = {
		"重":"1",
		"中":"2",
		"轻":"3",
		"良":"4",
		"优":"5",
	}
	return switcher.get(aircon, 00000000)