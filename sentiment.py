from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

from havenondemand.hodclient import *

word_track = raw_input("Search for: ")

api_key = "0af8447a-ccc3-4e10-907d-d7003a0ffde7"
hodClient = HODClient(api_key)

#consumer key, consumer secret, access token, access secret.
ckey="ClGrKpX3GGPiE5IwGjBfYP6vP"
csecret="Y6sFxA5owKjlytwvfupTgFgZC2irmeXUz2mvoEn533ImxlzxyU"
atoken="1651721448-dCRHaPeXIki70zcOo928XnFZyAkot25TPNyQBaG"
asecret="TLFGS9Gxxt6a6nfpgNnuPbqigHRjHX63VBhftTkgxlMbj"

class listener(StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]

            print tweet
            params = {}
            params["text"] = tweet
            params["language"] = "spa"
            response = hodClient.post_request(params, HODApps.ANALYZE_SENTIMENT, False)
            print response
        except:
            return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
try:
    twitterStream.filter(track=[word_track])
except:
    pass
