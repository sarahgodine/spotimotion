import sys
import csv

def main():
	# f = open('tracks.csv', 'r')
	w = open('time.csv', 'w')
	# reader = csv.reader(f, delimiter='\n')
	# for row in reader:
	# 	track = '\t'.join(row)
	# 	albumRes = sp.track(track)['album']
	# 	albumList.append(albumRes['id'])
	# for album in albumList:
	# 	timeRes = sp.album(album)
	# 	fullDate = str(timeRes['release_date'])

		# if (len(fullDate) == 10):			# Months
		# 	w.write(fullDate[5:7]+'\n')
		# else:
		# 	w.write('13\n')

		# w.write(str(fullDate[0:4])+'\n') 	# Years
	for i in range(0, 200):
		w.write('1'+'\n')
	for i in range(0, 200):
		w.write('2'+'\n')
	for i in range(0, 200):
		w.write('3'+'\n')
	for i in range(0, 200):
		w.write('4'+'\n')

	# f.close()
	w.close()

if __name__ == "__main__":
    main()