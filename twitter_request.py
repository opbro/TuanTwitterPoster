import json
from twython import Twython


Key_file_path="/root/venv0/key.json"

twitter = Twython(APP_KEY, APP_SECRET
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.update_status(status='See how easy using Twython is!')