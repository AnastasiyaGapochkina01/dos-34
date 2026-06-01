import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
OWNER = "AnastasiyaGapochkina01"
REPO = "jenkins_params_ex"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
BRANCH = "main"

params = {
    'ref': BRANCH
}

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.object'
}

def get_files():
    objects = []
    response = requests.get(API_URL, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        for item in data['entries']:
            if item['type'] == 'file':
                objects.append(item['name'])
    else:
        print(f"Error: {response.status_code}")
    return objects


files = get_files()
print(files)
