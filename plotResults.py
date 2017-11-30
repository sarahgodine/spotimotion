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
	plt.plot(timeList, featureList)
	plt.show()

	g = open('results.txt', 'a')
	g.write(str(linregress(np.array(timeList).astype(np.float), np.array(featureList).astype(np.float))) + '\n')
	g.close()

if __name__ == "__main__":
    main()