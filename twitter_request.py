#python twitter_request , arg1 will be the message posted to twitter..

import json
from twython import Twython
import time
import argparse

parser = argparse.ArgumentParser(description='Input Appliance.config file.')
parser.add_argument('-m',action='store',dest='message')
args = parser.parse_args()

message = args.message
print message
Key_file_path="/root/venv0/key.json"

with open(Key_file_path) as json_data:
	data = json.load(json_data)
json_data.close()



APP_KEY = data['API_KEY']
APP_SECRET = data['SUPER_SECRET_KEY']
OAUTH_TOKEN = data['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = data['OAUTH_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
twitter.update_status(status=message)