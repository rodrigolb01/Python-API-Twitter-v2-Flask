from user import User
from database import Database
from twitter_utils import get_request_token, get_oauth_verifier, get_access_token

Database.initialize(database='learning', user='postgres', password='m4a10121', host='localhost')

user_email = input('Email: ')

user = User.load_from_db(user_email)

if not user:
    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    print(access_token)

    user_first_name = input('user first_name: ')
    user_last_name = input('user last name: ')

    user = User(user_email, user_first_name, user_last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    user.save_to_db()

tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computer+filter:images'.encode('utf-8'))

for tweet in tweets['statuses']:
    print(tweet['text'])
