# tg-downloader

### **Approach**
1. **Telegram Bot API**:
   - Use the Telegram Bot API to interact with Telegram channels/groups.
   - The bot will require admin privileges in the group/channel to access restricted content.
   - If the bot cannot be added to the group/channel, you may need to use your own Telegram account with a session library like `Telethon` or `Pyrogram`.

2. **Session-Based Libraries**:
   - Libraries like `Telethon` or `Pyrogram` allow you to log in with your Telegram account and access restricted content.
   - These libraries can bypass restrictions by using your account's session.

3. **Downloading Videos**:
   - Once the bot or session has access to the video, it can download the file using the Telegram API.

4. **Ethical Considerations**:
   - Ensure you have permission to download the content.
   - Avoid violating Telegram's terms of service or the privacy of others.

---

### **Execution Plan**
1. **Set Up the Project**:
   - Use Python and the `Telethon` library for session-based access.
   - Create a script to log in to your Telegram account and fetch restricted videos.

2. **Authenticate with Telegram**:
   - Use Telegram's API credentials (API ID and API Hash) to authenticate.
   - Generate a session file for persistent login.

3. **Fetch and Download Videos**:
   - Use the `Telethon` library to fetch messages from the channel/group.
   - Identify video messages and download them.

4. **Save Videos Locally**:
   - Save the downloaded videos to a specified directory.

### **Implementation**

1. **Install Dependencies**:
   Run the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script**:
   Execute the script to start downloading videos:
   ```bash
   python downloader.py
   ```

3. **Replace Credentials**:
   Update config.py with your Telegram API credentials and phone number.