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

curFeature = 'valence'

def main():
	# g = open('results.txt', 'a')
	# g.write(curFeature + '\n')
	# g.close()
	f = open('tracks.csv', 'r')
	w = open('feature.csv', 'w')
	reader = csv.reader(f, delimiter='\n')
	for row in reader:
		track = '\t'.join(row)
		features = sp.audio_features(track)
		feature = features[0][curFeature]
		w.write(str(feature)+'\n')
	f.close()
	w.close()

if __name__ == "__main__":
    main()