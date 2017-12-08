import sys
import spotipy
sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'd070d273528b42fb944f2a65f846d78b'
secret = 'ce6c32a38f924906ae4fc3796c716b5e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

trackList = []

def main():
	# Query playlist on Spotify API and store tracks
	playlistUser = 'playlistgiants'
	playlistID = '6KOwiWg5zwrt83nEcx7HyI'
	results = sp.user_playlist(playlistUser, playlistID, fields="tracks")
	g = open('results.txt', 'a')
	g.write('\n' + playlistUser + '\t' + playlistID + '\n')
	g.close()
	tracks = results['tracks']
	add_tracks(tracks)
	while tracks['next']:
		tracks = sp.next(tracks)
		add_tracks(tracks)
	f = open('tracks.csv', 'w')
	for track in trackList:
		f.write(track + '\n')
	f.close()

def add_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		trackList.append(track['id'])

if __name__ == "__main__":
    main()
