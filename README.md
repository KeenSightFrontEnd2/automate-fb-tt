# Automate Facebook and TikTok Posts

- Run these commands for dependencies
    - `npm install`
    - `pip install`

- Development servers
    - `npm run dev`
    - `python app.py`

## Deployment

 - The app should be deployed to a service that supports Python, Flask and React.
 - The environment variables should be configured after deployment.

## Connecting to Facebook

- Create a Facebook App:
    - Go to the Facebook Developer Portal.
    - Create a new app.
    - Give necessary permissions for Business Account.

- Obtain Access Tokens:
    - Get the App ID and App Secret from your Facebook app settings.
    - Use the Facebook Graph API to obtain a user access token.
    - You may need to set up OAuth to allow users to authenticate and authorize your app to post on their behalf.

## Connecting to TikTok

- Create a TikTok Developer Account:
    - Sign up for a TikTok Developer Account.
    - Create a new app.

- Obtain API Keys:
    - Get the App ID and App Secret from your TikTok app settings.

## Environment Variables

The .env file is ready for putting the API Keys.