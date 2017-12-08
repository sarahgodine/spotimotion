import sys
import spotipy
sp = spotipy.Spotify()
import csv
from spotipy.oauth2 import SpotifyClientCredentials

trackList = []

def main():
	c = open('us-2017-10-03.csv', 'r')
	f = open('tracks.csv', 'a')
	firstLine = 1
	for line in c:
		if(firstLine != 1):
			items = line.split('/')
			trackID = items[-1]
			f.write(trackID)
		else:
			firstLine = 0
	c.close()
	f.close()

if __name__ == "__main__":
    main()