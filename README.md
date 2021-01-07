# Get YouTube Thumbnails

This broke in production and honestly I couldn't remember enough of the project to work it out. I've archived this project. And I've rebuilt it using Svelte and Netlify's serverless functions. It might still be a little rough around the edges.

<https://getyoutubethumbnails.netlify.app>

<https://github.com/edjw/get-youtube-thumbnails-svelte>
----

This is a web app that gets thumbnail images for YouTube videos. Paste in a YouTube URL and it gives you the thumbnails that are available for that video.

It works with URLs at these YouTube addresses: <code>https://www.youtube.com</code>, <code>https://youtube.com</code>, <code>https://youtu.be</code>, and <code>https://youtube-nocookie.com</code>.

When you submit a YouTube URL, you get back the image, a link to that image, and the original height and width of that image (even if it's scaled down on your screen size). You can also download the image with a YouTube play logo overlaid on the top.

## Use cases

**Linking to YouTube videos** when you can't or don't want to embed a video

- in emails
- in presentation slides (PowerPoint etc)
- in websites where you don't want any Javascript
- in websites where you want to minimise data transfers

## Installation

- `git clone` this repository
- `pipenv install`
- Add a file called `.env` something like this below. For local development, add another line saying `FLASK_DEBUG=1`

```env
SECRET_KEY="long-string-of-text"
YOUTUBE_API_KEY="your-google-api-key"
CLOUDINARY_CLOUD_NAME="your-cloudinary-cloud-name"
CLOUDINARY_API_KEY="your-cloudinary-api-key"
CLOUDINARY_API_SECRET="your-cloudinary-api-secret"
```

The WSGI `wsgi.py` file should look something like this (at least on [PythonAnywhere](https://www.pythonanywhere.com) where this is hosted).

```py

import sys

path = '/home/your-path-to/get-youtubethumbnails'
if path not in sys.path:
    sys.path.append(path)

from website import app as application
```

The site has only been tested on Flask 1.0.2 with Python 3.6 running on Python Anywhere.

## Built with

It relies heavily on the YouTube API for getting URLs to thumbnails and on [Cloudinary](https://cloudinary.com) for applying the play logos over the top and hosting that new image.

### Python

- Validate YouTube URLs
- Get the correct YouTube video ID for the different types of YouTube URLs
- Get the thumbnail data from YouTube's API using requests

### Flask

- Templating HTML with Jinja2
- Get URL out of form and send for processing in Python script
- Get results of Python script and put it into HTML

### Javascript

- Fill the input field with the demo link
