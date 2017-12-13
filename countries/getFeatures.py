import sys
import spotipy
from glob import glob
sp = spotipy.Spotify()
import csv
import argparse
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

cid = 'd070d273528b42fb944f2a65f846d78b'
secret = 'ce6c32a38f924906ae4fc3796c716b5e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

curFeature = 'valence'

def main():
	print(curFeature)
	for country_csv in glob('tracks/*.csv'):
		rows = []
		features = []
		values = []
		df = pd.read_csv(country_csv, dtype=object)

		for index, row in df.iterrows():
			track = row['track_id']
			features = sp.audio_features(track)
			print(track)
			try:
				feature = features[0][curFeature]
				values.append(feature)
			except TypeError:
				print("No features, skipping track")
				values.append(0.5)
			print(values)
		df.insert(loc=1, column=curFeature, value=values)
		df.to_csv(country_csv, sep=',', index=False)

if __name__ == "__main__":
    main()
