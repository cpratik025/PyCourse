import tweepy
import time

auth = tweepy.OAuthHandler('R1vSFKpLIGDK9XXOjg0JelPMB','qSgjjQPGMg9Y04HLyS0rdlYfpES6xrxG6hxXCT5OuAJSAkY3YL')
auth.set_access_token('180760287-gtJIbPbzXa8skPixdAkQaL5NXLHTvLH84u6vMP13','kBVsawg52kabyEdjLjJMeSSzHY7wHe4QATBoHDh97KVZB')

api = tweepy.API(auth)

public_Tweet = api.home_timeline()
#Grabs Twitter posts from timeline
for tweet in public_Tweet:
    print(tweet.text)

user =api.me()
#Prints follower count
print(user.followers_count)

def limit(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
#Looping through a follower
for followers in limit(tweepy.Cursor(api.followers).items()):
    print(followers.name)