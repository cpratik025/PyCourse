import tweepy
import time

auth = tweepy.OAuthHandler('M','L')
auth.set_access_token('N','O')

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
