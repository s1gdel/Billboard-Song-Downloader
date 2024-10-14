Top Songs Downloader

This Python program downloads the top songs from the Billboard Hot 100 chart and converts them into MP4 format using web scraping and YouTube.

Features:
- Fetches the current top songs from the Billboard Hot 100 chart by scraping the Billboard website.
- Uses `youtubesearchpython` to search for the corresponding YouTube video for each song.
- Downloads the video using `yt-dlp` in MP4 format.

Prerequisites:
- Python 3.x

Required Python libraries:
- `requests`
- `beautifulsoup4`
- `youtubesearchpython`
- `yt-dlp`
- `FFmpeg` (ensure it's installed and added to your system's PATH for video processing)

Install the necessary libraries by running:
pip install requests beautifulsoup4 youtubesearchpython yt-dlp

Make sure you have FFmpeg installed and added to your system's PATH.

How to Run the Program:
1. Run the script using:
   python top_songs_downloader.py

2. Input the number of top songs you want to download when prompted.

3. The program will search for the songs on YouTube and download them in MP4 format.

By default, the downloaded songs will be stored in:
C:\Users\subha\OneDrive\Desktop\Code\downloads

Customizing Download Path:
To change the download path, modify the download_path variable in the code.

Functions:
- scrape_billboard_hot_100(): Scrapes the top songs from the Billboard Hot 100 chart.
- display(): Displays the list of songs with their ranks, titles, and artists.
- searchYT(storedsongs): Searches for the songs on YouTube and returns their URLs.
- download_song(urls, download_path): Downloads the songs from the provided YouTube URLs using `yt-dlp`.

Example:

Input:
How many songs to download? 5

Output:  
The script will display the top 5 songs and download the corresponding YouTube videos in MP4 format.

Notes:
- Ensure your internet connection is stable during the download process.
- Check the YouTube URLs before downloading to avoid errors in case the search result is incorrect.
