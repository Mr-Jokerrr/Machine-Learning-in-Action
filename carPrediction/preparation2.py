import dataProcessing
from numpy import *
'''
write the combined data into a new csv file
'''

temp1 = dataProcessing.combineData("datasets\dailycheck_new.csv", "datasets\weather_new.csv")
print("writing the data 1 into a csv file now...")
dataProcessing.writeData(temp1, "datasets\\combinedData2.csv")
print("finished!")

'''
write the valid data into a new csv file
'''

temp2 = dataProcessing.validDataSet(dataProcessing.loadData("datasets\combinedData2.csv")\
	, "20170101", "20170409")
print("writing the data 2 into a csv file now...")
dataProcessing.writeData(temp2, "datasets\\validDataSet2.csv")
print("finished!")

'''
write the final csv file that will be used
'''

temp3 = dataProcessing.loadData('datasets\\validDataSet2.csv')
temp4 = []
for line in temp3:
	temp = []
	t = dataProcessing.calcuDays(line[0])
	temp.append(t)
	temp.extend(line[1:4])
	temp.extend(line[5:7])
	temp6 = dataProcessing.weatherDir(line[7])
	temp.append(temp6)
	temp6 = dataProcessing.airconDir(line[8])
	temp.append(temp6)
	temp.append(line[4])
	temp4.append(temp)

print("writing the data 3 into a csv file now...")
dataProcessing.writeData(temp4, "datasets\\finalDataSet2.csv")
print("finished!")
