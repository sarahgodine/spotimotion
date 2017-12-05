import sys
import spotipy
sp = spotipy.Spotify()
import csv
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'd070d273528b42fb944f2a65f846d78b'
secret = 'ce6c32a38f924906ae4fc3796c716b5e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

albumList = []

def main():
	f = open('tracks.csv', 'r')
	w = open('time.csv', 'w')
	reader = csv.reader(f, delimiter='\n')
	for row in reader:
		track = '\t'.join(row)
		albumRes = sp.track(track)['album']
		albumList.append(albumRes['id'])
	for album in albumList:
		timeRes = sp.album(album)
		fullDate = str(timeRes['release_date'])

		# if (len(fullDate) == 10):			# Months
		# 	w.write(fullDate[5:7]+'\n')
		# else:
		# 	w.write('13\n')

		w.write(str(fullDate[0:4])+'\n') 	# Years

	f.close()
	w.close()

if __name__ == "__main__":
    main()