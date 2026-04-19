from telethon import TelegramClient, sync
from telethon.tl.types import MessageMediaDocument
import os
from config import API_ID, API_HASH, PHONE_NUMBER

# Directory to save downloaded videos
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Initialize the Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

async def download_videos():
    # Connect to Telegram
    await client.start(phone=PHONE_NUMBER)
    print("Logged in successfully!")

    # Specify the channel or group username
    target = input("Enter the channel/group username or ID: ")

    # Fetch messages
    async for message in client.iter_messages(target):
        if message.video or isinstance(message.media, MessageMediaDocument):
            print(f"Downloading video: {message.id}")
            file_path = await message.download_media(file=DOWNLOAD_DIR)
            print(f"Saved to {file_path}")

    print("Download complete!")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(download_videos())