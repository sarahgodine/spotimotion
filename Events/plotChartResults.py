import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

featureList = []
timeList = []
tupleList = []

def main():
	tupleList = []
	f = open('feature.csv', 'r')
	reader = csv.reader(f, delimiter='\n')
	for row in reader:
		feature = '\t'.join(row)
		featureList.append(feature)
	f.close()

	g = open('time.csv', 'r')
	reader = csv.reader(g, delimiter='\n')
	for row in reader:
		time = '\t'.join(row)
		timeList.append(time)
	g.close()

	# Make tuples and sort
	for i in range(0, len(featureList)):
		tupleList.append((timeList[i], featureList[i]))
		tupleList.sort()
	i = 0
	for curTuple in tupleList:
		timeList[i] = curTuple[0]
		featureList[i] = curTuple[1]
		i+=1

	dayFeatures = []

	total = 0
	for i in range(0, 200):
		total += float(featureList[i])
	dayFeatures.append(total/200)
	total = 0
	for i in range(200, 400):
		total += float(featureList[i])
	dayFeatures.append(total/200)
	total = 0
	for i in range(400, 600):
		total += float(featureList[i])
	dayFeatures.append(total/200)
	total = 0
	for i in range(600, 800):
		total += float(featureList[i])
	dayFeatures.append(total/200)

	plt.scatter([1,2,3,4], dayFeatures)
	plt.xlabel("Day (09/30 - 10/03)")
	plt.ylabel("Valence")
	plt.show()

if __name__ == "__main__":
    main()