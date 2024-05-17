import requests

def downloader(url, path):
    with open(path, "wb") as a:
        response = requests.get(url)
        a.write(response.content)
        
videoLink = "video_url_link"
path = "name_of_video.mp4"

downloader(videoLink, path)

print("download complete")