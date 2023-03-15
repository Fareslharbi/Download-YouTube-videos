from pytube import YouTube

# Enter the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object
video = YouTube(url)

# Get the highest resolution stream
stream = video.streams.get_highest_resolution()

# Set the download path
path = "/Users/engfares/Desktop/Projects/DownloadVideoYouTube"

# Download the video
print("Downloading...")
stream.download(output_path=path)
print("Download completed.")