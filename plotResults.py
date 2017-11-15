import sys
import csv

def main():
	f = open('features.csv', 'r')
	g = open('time.csv', 'r')
	reader = csv.reader(f, delimiter='\n')
	for row in reader:
		track = '\t'.join(row)
		albumRes = sp.track(track)['album']
		albumList.append(albumRes['id'])
	for album in albumList:
		timeRes = sp.album(album)
		fullDate = timeRes['release_date']
		w.write(str(fullDate[0:4])+'\n') # Change character range to get year, month, or day
	f.close()
	w.close()


	# Make tuples and sort
	tupleList = []
	for i in range(0, len(featureList)):
    	tupleList.append((yearList[i], featureList[i]))
		tupleList.sort()
	i = 0
	for curTuple in tupleList:
    	yearList[i] = curTuple[0]
    	featureList[i] = curTuple[1]
    	i+=1

if __name__ == "__main__":
    main()