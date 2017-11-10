import sys
import pandas as pd
import spotipy
import json
import time
import matplotlib.pyplot as plt
sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials

def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

def add_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		trackList.append(track['id'])

trackList = []
featureList = []
yearList = []
albumList = []

curFeature = 'acousticness'

cid = 'd070d273528b42fb944f2a65f846d78b'
secret = 'ce6c32a38f924906ae4fc3796c716b5e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

# Query playlist on Spotify API and store tracks
results = sp.user_playlist('playlistgiants', '6KOwiWg5zwrt83nEcx7HyI', fields="tracks")
# results = sp.user_playlist('foreignsquid', '5E7xOR1eFzkQphQWrOAC5F', fields="tracks")
# results = sp.user_playlist('spotify', '37i9dQZF1DX3PIPIT6lEg5', fields="tracks")
# results = sp.user_playlist('nytimes', '74k3ZgRPQOUXS3EVBY1dZM', fields="tracks")
tracks = results['tracks']
add_tracks(tracks)
while tracks['next']:
	tracks = sp.next(tracks)
	add_tracks(tracks)

# Get audio features for tracks
for item in trackList:
	try:
		featureRes = sp.audio_features(item)
		featureList.append(featureRes[0][curFeature])
	except (ConnectionResetError, ProtocolError, ConnectionError):
		print("ConnectionResetError, song skipped\n")
		time.sleep(10)
	print(featureList)
# print(featureList)

# # Get year of each track
# for item in trackList:
# 	albumRes = sp.track(item)['album']
# 	albumList.append(albumRes['id'])
# print(albumList)
# for item in albumList:
# 	yearRes = sp.album(item)
# 	fullDate = yearRes['release_date']
# 	yearList.append(fullDate[0:4])

# # Make tuples and sort
# tupleList = []
# for i in range(0, len(featureList)):
#     tupleList.append((yearList[i], featureList[i]))
# tupleList.sort()
# i = 0
# for curTuple in tupleList:
#     yearList[i] = curTuple[0]
#     featureList[i] = curTuple[1]
#     i+=1

# # Plot the data
# plt.plot(yearList, featureList)
# plt.xlabel('year')
# plt.ylabel(curFeature)
# plt.show()

