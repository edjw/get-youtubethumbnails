from urllib.parse import urlparse
from base64 import b64encode
from requests import get
import nonexistent_image_base64


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


def check_non_existent_images(image_url):

    if b64encode(get(image_url).content) == nonexistent_image_base64.image_hash:
        return False

    else:
        return True


def create_youtube_image(video_id):

    max_resolution_image = "https://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"
    sd_default_image = "https://img.youtube.com/vi/" + video_id + "/sddefault.jpg"
    hq_default_image = "https://img.youtube.com/vi/" + video_id + "/hqdefault.jpg"
    mq_default_image = "https://img.youtube.com/vi/" + video_id + "/mqdefault.jpg"
    default_image = "https://img.youtube.com/vi/" + video_id + "/default.jpg"

    image_urls = [max_resolution_image, sd_default_image, hq_default_image, mq_default_image, default_image]

    for url in image_urls:
        if check_non_existent_images(url) == False:
            image_urls.remove(url)

    return image_urls


def get_youtube_thumbnail(yt_url):
    video_id = get_yt_video_id(yt_url)
    if video_id:
        return create_youtube_image(video_id)
    else:
        return False
