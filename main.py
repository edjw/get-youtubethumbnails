from urllib.parse import urlparse
from requests import get
from collections import OrderedDict

from config import Config


def validate_yt_url(parsed_url):
    valid_netlocs = [
        "www.youtube.com",
        "youtube.com",
        "youtu.be",
        "youtube-nocookie.com",
    ]
    netloc = parsed_url.netloc
    if netloc in valid_netlocs:
        return True
    else:
        return False


def get_yt_video_id(url):

    parsed_url = urlparse(url)

    if validate_yt_url(parsed_url) is False:
        return False

    domain = parsed_url.netloc
    if domain in ["www.youtube.com", "youtube.com"]:
        return str(parsed_url.query.lstrip("v="))
    elif domain == "youtu.be":
        return str(parsed_url.path.lstrip("/"))
    elif domain == "youtube-nocookie.com":
        return str(parsed_url.path.lstrip("/embed/"))


def get_thumbnails_data(video_id, yt_url):
    youtube_api_key = Config.YOUTUBE_API_KEY
    youtube_api_url = "https://www.googleapis.com/youtube/v3/videos?id="
    request_url = youtube_api_url + video_id + "&part=snippet&key=" + youtube_api_key

    response = get(request_url).json()
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


def get_youtube_thumbnail(yt_url):

    video_id = get_yt_video_id(yt_url)

    if video_id:
        thumbnails_data = get_thumbnails_data(video_id, yt_url)
        for key in thumbnails_data.items():
            url = key[1]["url"]
            url = url.replace("i.ytimg.com", "img.youtube.com")
            key[1]["url"] = url

        return thumbnails_data

    else:
        return False
