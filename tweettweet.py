import tweepy
import time

auth = tweepy.OAuthHandler('<your api key>', '<your api token>')
   
auth.set_access_token('<your consumer key>', '<your consumer token>')

api = tweepy.API(auth)

user = api.me()

# print(user.name)
# print(user.followers_count)

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)
        except StopIteration:
            break

search_str = 'Musk'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_str).items(2):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(f'Tweepy error: {e.reason}')
    except StopIteration:
        break


#Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'AFollowerName':
#         follower.follow()
#         break


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)