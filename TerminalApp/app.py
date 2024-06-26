import os
import json
import argparse
import requests
from dotenv import load_dotenv
from authlib.integrations.requests_client import OAuth2Session

# Load environment variables from .env file
load_dotenv()

# OAuth configurations
FACEBOOK_APP_ID = os.getenv('FACEBOOK_APP_ID')
FACEBOOK_APP_SECRET = os.getenv('FACEBOOK_APP_SECRET')
TIKTOK_APP_ID = os.getenv('TIKTOK_APP_ID')
TIKTOK_APP_SECRET = os.getenv('TIKTOK_APP_SECRET')

def get_facebook_token():
    session = OAuth2Session(FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
    token = session.fetch_token(
        'https://graph.facebook.com/v20.0/oauth/access_token',
        authorization_response='your_authorization_response'
    )
    return token

def get_tiktok_token():
    session = OAuth2Session(TIKTOK_APP_ID, TIKTOK_APP_SECRET)
    token = session.fetch_token(
        'https://open-api.tiktok.com/oauth/access_token/',
        authorization_response='your_authorization_response'
    )
    return token

def post_facebook(message, image_path, token):
    url = 'https://graph.facebook.com/me/photos'
    params = {'access_token': token['access_token'], 'caption': message}
    files = {'source': open(image_path, 'rb')}
    response = requests.post(url, params=params, files=files)
    return response.json()

def post_tiktok(video_path, description, token):
    url = 'https://open-api.tiktok.com/share/video/upload/'
    params = {'access_token': token['access_token'], 'description': description}
    files = {'video': open(video_path, 'rb')}
    response = requests.post(url, params=params, files=files)
    return response.json()

def post_facebook_marketplace(data, token):
    url = 'https://graph.facebook.com/me/photos'
    params = {
        'access_token': token['access_token'],
        'caption': data['description'],
        'title': data['title'],
        'price': data['price'],
        'currency': data['currency'],
        'location': data['location']
    }
    files = {'source': open(data['image_path'], 'rb')}
    response = requests.post(url, params=params, files=files)
    return response.json()

def post_tiktok_marketplace(data, token):
    url = 'https://open-api.tiktok.com/share/video/upload/'
    params = {
        'access_token': token['access_token'],
        'description': data['description'],
        'title': data['title'],
        'price': data['price'],
        'currency': data['currency'],
        'location': data['location']
    }
    files = {'video': open(data['video_path'], 'rb')}
    response = requests.post(url, params=params, files=files)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Post to Facebook and TikTok")
    parser.add_argument('--json_file_path', type=str, required=True, help="Path to the JSON file containing the post data")
    args = parser.parse_args()

    with open(args.json_file_path, 'r') as file:
        data = json.load(file)

    facebook_token = get_facebook_token()
    tiktok_token = get_tiktok_token()

    for post_data in data:
        platform = post_data.get('platform')
        post_type = post_data.get('type')

        if platform == 'facebook':
            if post_type == 'post':
                post_facebook(post_data['message'], post_data['image_path'], facebook_token)
            elif post_type == 'marketplace':
                post_facebook_marketplace(post_data, facebook_token)
        elif platform == 'tiktok':
            if post_type == 'post':
                post_tiktok(post_data['video_path'], post_data['description'], tiktok_token)
            elif post_type == 'marketplace':
                post_tiktok_marketplace(post_data, tiktok_token)

if __name__ == '__main__':
    main()
