from pytube import YouTube

def downloader(url, path):
    try:
        youtubeCore = YouTube(url)
        stream = youtubeCore.streams.get_highest_resolution()
        stream.download(output_path=path)
        print("dowload complete")
    except Exception as err:
        print(err)
        
videoLink = "_your_video_link"
path = "any_folder_path"
downloader(videoLink, path)