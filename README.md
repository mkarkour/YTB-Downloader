# YouTube Video Downloader

This Python script allows you to download YouTube videos by providing the video's URL. It uses the PyTube library for downloading videos.

## Prerequisites

- Python 3.x installed on your system.
- Install the PyTube library using pip: `pip install pytube`.

## Usage

1. Run the script using Python: `python script.py`.

2. Enter the path where you want to save the downloaded videos when prompted.

3. Input the URL of the YouTube video you want to download.

4. Click the "Confirm" button, and the video will be downloaded to the specified path.

## How it Works

1. The script takes the user's input for the URL of the YouTube video.

2. It checks if the "youtube video" directory exists in the specified path and creates it if not.

3. It then uses PyTube to download the highest resolution version of the video to the specified path.

4. After a successful download, it provides a confirmation message.

## User Interface (Tkinter)

- The script provides a simple graphical user interface (GUI) created using the Tkinter library.

- Users can enter the video URL into the input field and click the "Confirm" button to initiate the download.

## Author

This script was created by me. 

Feel free to use and customize it for your video downloading needs. You can further enhance it by adding more features or error handling based on your requirements.

Enjoy downloading your favorite YouTube videos!
