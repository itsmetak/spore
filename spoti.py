import re

import spotipy
import spotipy.util as util

def loginSpotify(creds):
    c = open(creds,'r').read().strip().split(' ')
    token = util.prompt_for_user_token(c[0],c[1],
                                       client_id=c[2],
                                       client_secret=c[3],
                                       redirect_uri=c[4])

    sp = spotipy.Spotify(auth=token)
    return sp

def cleanTrackList(tracklist):
    tracklist = [ track.split('[')[0] for track in tracklist ]
    tracklist = [ re.sub(r"[^a-zA-Z0-9 ]","",track) for track in tracklist ]

    return tracklist
    

def createPlaylist(name):
    plist = sp.user_playlist_create('davidtkcs', name)
    return plist

def addSongsToPlaylist(plist, tracklist):
    
    tracklist = cleanTrackList(tracklist)
    tracks = []
    
    for track in tracklist:
        song = sp.search(track,limit=1)
        try:
            tracks.append(song['tracks']['items'][0]['uri'])
        except:
            print(f'Couldn\'t find {track}.')

    pl =  plist['uri']
    sp.user_playlist_add_tracks('davidtkcs', tracks=tracks, playlist_id=pl)


if __name__ == '__main__':
    l = ['Harvey Danger - Flagpole Sitta [Alternative]', 'Depeche Mode - Enjoy The Silence [Synthpop]', 'Peter Bjorn and John - Young Folks [Indie Pop]', 'The Weight - The Band [Folk]', 'Chino Cappin - Slime [Hip-Hop]', 'Mobb Deep - Shook Ones [Hip-Hop]', 'Stevie Wonder - Superstition [R&B]', 'Robert Plant & Alison Krauss - Fortune Teller [ rock folk ]', 'Dead Kennedys - Pull My Strings [Punk Rock]', 'RX Bandits - Apparition - Audiotree Live [Prog Rock]', "DVDA - Now You're a Man [Rock/South Park]"]
    sp = loginSpotify('spotcreds.txt')
    pl = createPlaylist('test')
    addSongsToPlaylist(pl,l)
