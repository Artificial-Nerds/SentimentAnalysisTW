from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import sys

word_track = raw_input("Introduce termino de busqueda: ")

#consumer key, consumer secret, access token, access secret.
ckey="pp9t5cw3I2EdxxptSkdZ0M2Y6"
csecret="rn6EZyc8LSWqQvPnlPeFOnr0lwmJ5dkFDR7hTFsIq8ZBq6RzxY"
atoken="1651721448-6GobP1KBQr7fjjiMA5jX1Zd4NEbzvtLGLxChlaH"
asecret="B8ppnUgYrup6gX1MMEnPG9XPWu4HceqUTcjEOmBk9JRN8"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]

            print(tweet)
        except:
            return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[word_track])
