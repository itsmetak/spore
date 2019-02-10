import praw

def loginReddit(creds):
    c = open(creds,'r').read().strip().split(' ')
    reddit = praw.Reddit(client_id=c[0],
                         client_secret=c[1],
                         username=c[2],
                         password=c[3],
                         user_agent=c[4])

    return reddit

def getTopSongs(reddit, lim=25, time='day'):

    music = reddit.subreddit('Music')
    top_music = music.top(time_filter=time,limit=100)

    songs = []

    for music in top_music:
        try:
            flair = music.link_flair_richtext[0]['t']
        except IndexError:
            continue
        title = music.title
        if flair == 'music streaming':
            songs.append(title)

    return songs[:lim]

if __name__ == '__main__':
    reddit = loginReddit('creds.txt')
    songs = getTopSongs(reddit)
    print(songs)
