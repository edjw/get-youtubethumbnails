from urllib.parse import urlparse
from requests import get
from collections import OrderedDict

from config import YouTube_Config


def validate_yt_url(parsed_url):
    valid_netlocs = [
        "www.youtube.com",
        "youtube.com",
        "youtu.be",
        "youtube-nocookie.com",
        "www.youtube-nocookie.com",
    ]
    netloc = parsed_url.netloc
    if netloc == "":
        netloc = parsed_url.path.split("/")[0]

    if netloc in valid_netlocs:
        return True
    else:
        return False


def get_yt_video_id(url):

    parsed_url = urlparse(url, "https")
    if validate_yt_url(parsed_url) is False:
        return False

    domain = parsed_url.netloc
    if domain == "":
        domain = parsed_url.path.split("/")[0]

    if domain in ["www.youtube.com", "youtube.com"] and parsed_url.query.startswith(
        "v="
    ):
        return str(parsed_url.query.split("v=")[1])
    elif domain == "youtu.be":
        return str(parsed_url.path.split("/")[1])
    elif domain in ["youtube-nocookie.com", "www.youtube-nocookie.com"]:
        return str(parsed_url.path.split("/")[2])


def get_thumbnails_data(video_id, yt_url):
    youtube_api_key = YouTube_Config.YOUTUBE_API_KEY
    youtube_api_url = "https://www.googleapis.com/youtube/v3/videos?id="
    request_url = youtube_api_url + video_id + "&part=snippet&key=" + youtube_api_key

    response = get(request_url).json()

    if len(response["items"]) > 0:
        thumbnails = response["items"][0]["snippet"]["thumbnails"]
        thumbnails_data = OrderedDict()

        for item in thumbnails.items():
            thumbnails_data.update(
                {
                    item[0]: {
                        "url": item[1]["url"],
                        "height": item[1]["height"],
                        "width": item[1]["width"],
                    }
                }
            )

        thumbnails_data = OrderedDict(reversed(list(thumbnails_data.items())))

        return thumbnails_data

    else:
        return False


def get_youtube_thumbnail(yt_url):

    video_id = get_yt_video_id(yt_url)

    if video_id:
        thumbnails_data = get_thumbnails_data(video_id, yt_url)

        if thumbnails_data:
            # This section only necessary because i.ytimg.com isn't whitelisted for outbound connections on Python Anywhere's free tier
            for key in thumbnails_data.items():
                url = key[1]["url"]
                url = url.replace("i.ytimg.com", "img.youtube.com")
                key[1]["url"] = url

            return thumbnails_data

    else:
        return False
