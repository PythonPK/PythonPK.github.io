import yt_dlp

def download_yt_video(url):
    ydl_options = {
        "format": "bestvideo[height<=1080]+bestaudio/best",
        "noplaylist": True,
        "outtmpl": 'C:\\Users\\kingp\\OneDrive\\Videos\\%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the URL of the video you want to download: ")
    download_yt_video(video_url)
