from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = getenv("SECRET_KEY")
    YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY")
    CLOUDINARY_CLOUD_NAME = getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = getenv("CLOUDINARY_API_SECRET")
