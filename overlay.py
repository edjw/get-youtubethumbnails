from config import Config
from urllib.parse import urlparse
import cloudinary


cloudinary.config.update = {
    "cloud_name": Config.CLOUDINARY_CLOUD_NAME,
    "api_key": Config.CLOUDINARY_API_KEY,
    "api_secret": Config.CLOUDINARY_API_SECRET,
}


def overlay(image_url):
    image_size_name = urlparse(image_url).path.split("/")[-1]

    if image_size_name == "maxresdefault.jpg":
        width = "2.0"

    elif image_size_name == "sddefault.jpg":
        width = "1.4"

    elif image_size_name == "hqdefault.jpg":
        width = "1.0"

    elif image_size_name == "mqdefault.jpg":
        width = "0.7"

    elif image_size_name == "default.jpg":
        width = "0.35"

    else:
        width = "1.0"

    overlay = "logos:youtube_logo"

    new_image = cloudinary.CloudinaryImage(image_url).image(
        secure=True, sign_url=True, type="fetch", overlay=overlay, width=width
    )

    new_image = new_image.lstrip('<img src="')
    new_image = new_image.rstrip('"/>')

    return new_image

