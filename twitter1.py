import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_user_timeline():
    print('')
    acct = input('Enter Twitter Account:')
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    #headers = dict(connection.getheaders())
    #print('Remaining', headers['x-rate-limit-remaining'])
    return data


def json_user_timeline():
    data = get_user_timeline()
    datadict = {'statuses': json.loads(data)} # json.loads(data) is a list of statuses
    return datadict
