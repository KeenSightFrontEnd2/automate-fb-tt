# Social Media Post Uploader

This application allows you to post messages, images, and videos to Facebook and TikTok, as well as their respective marketplaces, from a JSON file.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Create a `.env` file with your credentials:

### .env file

```
FACEBOOK_APP_ID=your_facebook_app_id
FACEBOOK_APP_SECRET=your_facebook_app_secret
TIKTOK_APP_ID=your_tiktok_app_id
TIKTOK_APP_SECRET=your_tiktok_app_secret
```

## Running the App

1. Install Dependencies:
   Ensure you have Python and pip installed. Navigate to your project directory and install the dependencies:

```
pip install -r requirements.txt
```

2. Run the App:
   Execute the script with the JSON file path as an argument:

```
python app.py --json_file_path sample_input.json
```