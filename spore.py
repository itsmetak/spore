from red import *
from spo import *

reddit = loginReddit('creds.txt')
songs = getTopSongs(reddit)

print('Top songs of the day:')
for i, song in enumerate(songs):
    print(f'{i+1}. {song}')

sp = loginSpotify('spotcreds.txt')
pl = createPlaylist(sp, 'dailytop-reddit')
addSongsToPlaylist(sp, pl,songs)