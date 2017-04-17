import dataProcessing
from numpy import *
'''
write the combined data into a new csv file
'''
temp1 = dataProcessing.combineData("datasets\dailycheck.csv", "datasets\weather_new.csv")
print("writing the data 1 into a csv file now...")
dataProcessing.writeData(temp1, "datasets\\combinedData.csv")
print("finished!")

'''
write the valid data into a new csv file
'''
temp2 = dataProcessing.validDataSet(dataProcessing.loadData("datasets\combinedData.csv")\
	, "20160101", "20161130")
print("writing the data 2 into a csv file now...")
dataProcessing.writeData(temp2, "datasets\\validDataSet.csv")
print("finished!")

'''
write the final csv file that will be used
'''
temp3 = dataProcessing.loadData('datasets\\validDataSet.csv')
temp4 = []
for line in temp3:
	temp = []
	t = dataProcessing.calcuDays(line[0])
	temp.append(t)
	temp.extend(line[1:4])
	temp.extend(line[5:7])
	temp.extend(line[9:11])
	temp.append(line[4])
	temp4.append(temp)
print("writing the data 3 into a csv file now...")
dataProcessing.writeData(temp4, "datasets\\finalDataSet.csv")
print("finished!")