import requests
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch
import yt_dlp
import os

# Function to scrape Billboard Hot 100 songs
def scrape_billboard_hot_100():
    url = 'https://www.billboard.com/charts/hot-100/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    songs = []
    artists = []

    # Find all song titles and artists from the Billboard Hot 100 page
    for song in soup.select('li ul li h3'):
        songs.append(song.get_text(strip=True))
    
    for artist in soup.select('li ul li span.c-label'):
        artists.append(artist.get_text(strip=True))

    # Return a list of tuples containing song title and artist
    return list(zip(songs[:100], artists[:100]))  # Limit to top 100

# Get the number of songs to download
numsongs = int(input("How many songs to download? "))

# Get top songs using web scraping
storedsongs = scrape_billboard_hot_100()[:numsongs]

# Display the songs
def display():
    for rank, (title, artist) in enumerate(storedsongs, 1):
        print(f"{rank}.{title} by {artist}")

display()

# Search songs on YouTube
def searchYT(storedsongs):
    urls = []
    for title, artist in storedsongs:
        ytSearch = VideosSearch(f"{title} {artist}", limit=1)
        result = ytSearch.result()
        videoURL = result['result'][0]['link']
        urls.append(videoURL)
    return urls

# Get YouTube URLs for the songs
urls = searchYT(storedsongs)

# Set download path
download_path = r"DESIRED PATH HERE"

# Download the songs using yt-dlp
def download_song(urls, download_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Ensure MP4 video and M4A audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4', 
        }],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Include the download path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            ydl.download([url])

# Download the videos from YouTube URLs
download_song(urls, download_path)
