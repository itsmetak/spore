import praw

def loginReddit(creds):
    c = open(creds,'r').read().strip().split(' ')
    reddit = praw.Reddit(client_id=c[0],
                         client_secret=c[1],
                         username=c[2],
                         password=c[3],
                         user_agent=c[4])

    return reddit

def getTopSongs(reddit, lim=15, time='day'):

    music = reddit.subreddit('Music')
    top_music = music.top(time_filter=time,limit=lim)

    songs = []

    for music in top_music:
        flair = music.link_flair_richtext[0]['t']
        title = music.title
        if flair == 'music streaming':
            songs.append(title)

    return songs

if __name__ == '__main__':
    reddit = loginReddit('creds.txt')
    songs = getTopSongs(reddit)
    print(songs)
