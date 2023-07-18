import os
import time
import asyncio
from datetime import datetime
from telegram import Bot
from telegram import InputFile
import winsound

# Initialize your Telegram bot
bot_token = '6348598xxxxxxxxxxxxxkDUE0'
bot = Bot(token=bot_token)

# Specify the main folder path where the images are saved
main_folder_path = r'C:\Users\Lenovo\Desktop\Khanfar_systems_v3\ANPR_General\ANPR_V1\bin\ANPR_Image\Cam-2'

# Define last_processed_time as a global variable
last_processed_time = 0

# File to store the last_processed_time
time_file = 'last_processed_time.txt'

# Load the last_processed_time from the file
if os.path.exists(time_file):
    with open(time_file, 'r') as f:
        last_processed_time = float(f.read())

async def send_new_images():
    global last_processed_time  # Access the global variable

    # Get the current date and time
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%y")
    # Get the folder path for the current date
    folder_path = os.path.join(main_folder_path, current_date)

    # Check if the folder for the current date exists
    if os.path.exists(folder_path):
        # Get the list of files in the folder
        files = os.listdir(folder_path)
        # Sort the files by modification time (oldest to newest)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

        for file in files:
            if file.endswith('.jpg'):
                file_path = os.path.join(folder_path, file)
                modified_time = os.path.getmtime(file_path)

                # Check if the image is modified after the last processed time
                if modified_time > last_processed_time:
                    # Send the image to your Telegram bot
                    with open(file_path, 'rb') as f:
                        await bot.send_photo(chat_id='81xxxxx20', photo=InputFile(f))

                    # Extract the desired text
                    text = file.split('.')[0].replace('-', ' ')

                    # Display the text in the terminal
                    print(f"{text} ---------------- captured by MKhanfar Systems on: {current_datetime}")

                    # Send a separate message with the text in the Telegram chat
                    await bot.send_message(chat_id='815080920', text=f"{text} ---------------- captured by MKhanfar Systems on: {current_datetime}")

                    # Play motherboard beep sound
                    winsound.Beep(1000, 200)

                    # Update the last processed time
                    last_processed_time = modified_time

                    # Save the last processed time to the file
                    with open(time_file, 'w') as f:
                        f.write(str(last_processed_time))

                    # Optional: Delete the image file after sending
                    # os.remove(file_path)

async def main():
    # Display welcome message
    print("Welcome to KHANFAR Systems")

    while True:
        await send_new_images()
        await asyncio.sleep(5)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
