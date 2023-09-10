import os
import telebot
import google.auth
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

# Set up YouTube API client
creds = Credentials.from_authorized_user_file('client_secret_854211011522-stj2qbjkrk1nu5mqtgouucqqad7u6lg0.apps.googleusercontent.com.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
youtube = build('youtube', 'v3', credentials=creds)

# Set up Telegram bot
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(regexp='^https://www\.youtube\.com/shorts/.*$')
def download_short(message):
    link = message.text
    video_id = link.split('?v=')[1]
    # Call YouTube API to get video details
    try:
        response = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()
        title = response['items'][0]['snippet']['title']
        # Download video
        os.system(f'youtube-dl -f mp4 -o "{title}.mp4" {link}')
        # Send video to user
        with open(f'{title}.mp4', 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)
        # Clean up downloaded file
        os.remove(f'{title}.mp4')
    except HttpError as e:
        print(f'An error occurred: {e}')
        bot.send_message(message.chat.id, 'Error: could not download video.')

bot.polling()
