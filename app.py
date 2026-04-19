from flask import Flask, request, render_template
from telethon import TelegramClient, sync
from telethon.tl.types import MessageMediaDocument
import os
from config import API_ID, API_HASH, PHONE_NUMBER

app = Flask(__name__)

# Directory to save downloaded videos
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Initialize the Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    target = request.form['target']
    video_ids = request.form.getlist('video_ids')

    with client:
        async def fetch_and_download():
            async for message in client.iter_messages(target):
                if str(message.id) in video_ids:
                    if message.video or isinstance(message.media, MessageMediaDocument):
                        file_path = await message.download_media(file=DOWNLOAD_DIR)
                        print(f"Downloaded: {file_path}")

        client.loop.run_until_complete(fetch_and_download())

    return "Download complete!"

if __name__ == '__main__':
    app.run(debug=True)