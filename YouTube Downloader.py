import os
import yt_dlp

def download_youtube(url: str, file_format: str = "mp3"):
    """
    Downloads a YouTube video as MP3 or MP4 into a 'downloads' folder.
    
    :param url: The YouTube URL.
    :param file_format: 'mp3' or 'mp4'.
    """
    # Ensure a "downloads" folder exists
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    # Options for yt-dlp
    ydl_opts = {
        # Save files inside "downloads" folder with the video's title
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    # MP3 or MP4
    if file_format.lower() == "mp3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        })

    # Perform the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    print("Welcome to the YouTube Downloader!")
    print("This will download videos to a 'downloads' folder in the same directory.")
    
    while True:
        youtube_link = input("\nEnter a YouTube link (or type 'q' to quit): ").strip()
        if youtube_link.lower() in ["q", "quit", "exit"]:
            break
        
        choice = input("Download as MP3 or MP4? ").strip().lower()
        if choice not in ["mp3", "mp4"]:
            print("Invalid choice, defaulting to MP3...")
            choice = "mp3"
        
        download_youtube(youtube_link, file_format=choice)
        print("\nDownload finished!")
        
        another = input("Would you like to download another video? (yes/no): ").strip().lower()
        if another not in ["y", "yes"]:
            break
    
    print("\nThanks for using the YouTube Downloader. Goodbye!")


if __name__ == "__main__":
    main()