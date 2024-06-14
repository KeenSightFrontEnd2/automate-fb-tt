from flask import Flask, redirect, request, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Enable CORS for API routes
app.secret_key = os.getenv('SECRET_KEY')

oauth = OAuth(app)

# Configure Facebook OAuth
facebook = oauth.register(
    name='facebook',
    client_id=os.getenv('FACEBOOK_APP_ID'),
    client_secret=os.getenv('FACEBOOK_APP_SECRET'),
    access_token_url='https://graph.facebook.com/v20.0/oauth/access_token',
    authorize_url='https://www.facebook.com/v20.0/dialog/oauth',
    client_kwargs={'scope': 'email public_profile user_posts publish_actions'}
)

# Configure TikTok OAuth
tiktok = oauth.register(
    name='tiktok',
    client_id=os.getenv('TIKTOK_APP_ID'),
    client_secret=os.getenv('TIKTOK_APP_SECRET'),
    authorize_url='https://open-api.tiktok.com/platform/oauth/connect/',
    access_token_url='https://open-api.tiktok.com/oauth/access_token/',
    client_kwargs={'scope': 'user.info.basic,video.upload'}
)

@app.route('/login/facebook')
def login_facebook():
    redirect_uri = url_for('authorize_facebook', _external=True)
    return facebook.authorize_redirect(redirect_uri)

@app.route('/authorize/facebook')
def authorize_facebook():
    token = facebook.authorize_access_token()
    resp = facebook.get('https://graph.facebook.com/me?fields=id,name,email')
    profile = resp.json()
    session['facebook_token'] = token
    session['facebook_user'] = profile
    return redirect('/')

@app.route('/login/tiktok')
def login_tiktok():
    redirect_uri = url_for('authorize_tiktok', _external=True)
    return tiktok.authorize_redirect(redirect_uri)

@app.route('/authorize/tiktok')
def authorize_tiktok():
    token = tiktok.authorize_access_token()
    resp = tiktok.get('https://open-api.tiktok.com/user/info/')
    profile = resp.json()
    session['tiktok_token'] = token
    session['tiktok_user'] = profile
    return redirect('/')

# Example route to post to Facebook
@app.route('/api/post_facebook', methods=['POST'])
def post_facebook():
    token = session.get('facebook_token')
    if not token:
        return jsonify({'error': 'User not authenticated'}), 401

    data = request.json
    message = data.get('message', '')

    url = 'https://graph.facebook.com/me/feed'
    params = {'access_token': token['access_token'], 'message': message}
    response = requests.post(url, params=params)
    return jsonify(response.json())

# Example route to post to TikTok
@app.route('/api/post_tiktok', methods=['POST'])
def post_tiktok():
    token = session.get('tiktok_token')
    if not token:
        return jsonify({'error': 'User not authenticated'}), 401

    data = request.json
    video_url = data.get('video_url', '')

    url = 'https://open-api.tiktok.com/share/video/upload/'
    params = {'access_token': token['access_token'], 'video_url': video_url}
    response = requests.post(url, params=params)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
