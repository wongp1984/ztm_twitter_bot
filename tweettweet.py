import tweepy
import time

auth = tweepy.OAuthHandler('LOkjYnhOINnTVPXSGjonpudex', 'edeBNJiOuNmyIyQrGuVXCTrspYqTjvZlIaSkDQCeNJIlTfxoPj')
   
auth.set_access_token('1561269627254079488-2Wd9K3nPP8blBn9mF1pN1rNgl0M0dn', 'JlIwU2i17rYVJQn6d337w9G9C9kh8AAXsu39baVDMo2n9')

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