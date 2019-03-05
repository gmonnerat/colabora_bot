from decouple import config

consumer_key = config('CONSUMER_KEY', default="changeme")
consumer_secret = config('CONSUMER_SECRET', default="changeme")
access_token = config('ACCESS_TOKEN', default="changeme")
access_token_secret = config('ACCESS_TOKEN_SECRET', default="changeme")
