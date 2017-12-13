import sys
import spotipy
sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

cid = 'd070d273528b42fb944f2a65f846d78b'
secret = 'ce6c32a38f924906ae4fc3796c716b5e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

trackList = []
playlistDict = {
 	'argentina': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMMy2roB9myp',
	'australia':'spotify:user:spotifycharts:playlist:37i9dQZEVXbJPcfkRz0wJ0',
	'austria': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKNHh6NIXu36',
	'belgium': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJNSeeHswcKB',
	'bolivia':'spotify:user:spotifycharts:playlist:37i9dQZEVXbJqfMFK4d691',
	'brazil':'spotify:user:spotifycharts:playlist:37i9dQZEVXbMXbN3EUUhlg',
	'canada': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKj23U1GF4IR',
	'chile': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbL0GavIqMTeb',
	'colombia': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbOa2lmxNORXQ',
	'costa_rica': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMZAjGMynsQX',
	'czech_republic': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbIP3c3fqVrJY',
	'denmark': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbL3J0k32lWnN',
	'dominican_republic': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKAbrMR8uuf7',
	'ecuador': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJlM6nvL1nD1',
	'el_salvador': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLxoIml4MYkT',
	'estonia': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLesry2Qw2xS',
	'finland': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMxcczTSoGwZ',
	'france': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbIPWwFssbupI',
	'germany': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJiZcmkrIHGU',
    'global': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMDoHDwVN2tF',
	'greece': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJqdarpmTJDL',
	'guatemala': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLy5tBFyQvd4',
	'honduras': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJp9wcIM9Eo5',
	'hong_kong': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLwpL8TjsxOG',
	'hungary': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbNHwMxAkvmF8',
	'iceland': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKMzVsSGQ49S',
	'indonesia': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbObFQZ3JLcXt',
	'ireland': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKM896FDX8L1',
	'italy': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbIQnj7RRhdSX',
	'japan': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKXQ4mDTEBXq',
	'latvia': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJWuzDrTxbKS',
	'lithuania': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMx56Rdq5lwc',
	'malaysia': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJlfUljuZExa',
	'mexico': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbO3qyFxbkOE1',
	'netherlands': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKCF6dqVpDkS',
	'new_zealand': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbM8SIrkERIYl',
	'norway': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJvfa0Yxg7E7',
	'panama': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKypXHVwk1f0',
	'paraguay': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbNOUPGj7tW6T',
	'peru': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJfdy5b0KP7W',
	'philippines': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbNBz9cRCSFkY',
	'poland': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbN6itCcaL3Tt',
	'portugal': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKyJS56d1pgi',
	'singapore': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbK4gjvS1FjPY',
	'slovakia': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbKIVTPX9a2Sb',
	'spain': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbNFJfN1Vw8d9',
	'sweden': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLoATJ81JYXz',
	'switzerland': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJiyhoAPEfMK',
	'taiwan': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMnZEatlMSiu',
	'thailand': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMnz8KIWsvf9',
	'turkey': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbIVYVBNw9D5K',
	'united_kingdom': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLnolsZ8PSNw',
	'united_states': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLRQDuF5jeBp',
	'uruguay': 'spotify:user:spotifycharts:playlist:37i9dQZEVXbMJJi3wgRbAy'
}

def main():
	# Query playlist on Spotify API and store tracks
	# playlistUser = 'playlistgiants'
	# playlistID = '6KOwiWg5zwrt83nEcx7HyI'
    countries = list(playlistDict.keys())
    playlistUser = 'spotifycharts'
    for country in countries:
        print(country)
        playlistID = playlistDict[country].split(':')[-1]
        results = sp.user_playlist(playlistUser, playlistID, fields="tracks")
        tracks = results['tracks']
		# print(tracks)

        g = open('tracks/{0}.csv'.format(country),'w')
        g.write('track_id\n')
        add_tracks(tracks, g)
        g.close()
        while tracks['next']:
            tracks = sp.next(tracks)
            add_tracks(tracks)

def add_tracks(tracks, fname):
    trackList = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
        trackList.append(track['id'])
    for track in trackList:
        print(track)
        fname.write(track + '\n')

if __name__ == "__main__":
    main()
