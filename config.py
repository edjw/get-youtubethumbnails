from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = getenv("SECRET_KEY")
    YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY")
