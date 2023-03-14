import os
import json


if os.name == 'posix':
    path = '/etc/t-learning/config.json'
else:
    path = './app/core/config.json'

if not os.path.exists(path):
    raise Exception(f'The config file config.json is missing')

def get_config(filename: str = path):
    config = json.loads(open(filename, 'r').read())
    return config

cfg = get_config()
openai_apikey = cfg.get('api').get('openai_apikey')
