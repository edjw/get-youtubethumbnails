# Get YouTube Thumbnails

This is a web app that gets thumbnail images for YouTube videos. Paste in a YouTube URL and it gives you the thumbnails that are available for that video.

It works with URLs at these YouTube addresses: <code>https://www.youtube.com</code>, <code>https://youtube.com</code>, <code>https://youtu.be</code>, and <code>https://youtube-nocookie.com</code>.

When you submit a YouTube URL, you get back the image, a link to that image, and the original height and width of that image (even if it's scaled down on your screen size).

## Use cases

**Linking to YouTube videos** when you can't or don't want to embed a video

- in emails
- in websites where you don't want any Javascript
- in websites where you want to minimise data transfers

## Installation
- `git clone` this repository
- `pipenv install`
- Add a file called `.env` with `SECRET_KEY=long-string-of-text` and `YOUTUBE_API_KEY="your-google-api-key".` For local development, add another line saying `FLASK_DEBUG=1`

## Future development

Add the option of overlaying [a play button](https://png2.kisspng.com/sh/3143cad342bc76a1b9480718d3f6da08/L0KzQYm3VMAzN5N4iZH0aYP2gLBuTfNwdaF6jNd7LXnmf7B6TglwfaV6etc2cHzkiX7plgR1d58ye95ycD3kgsW0kPxigV5njeZ9b36wRbLqUfQ1bGM6UaQ6ZEWxR4KAV8E2QWM2TaQ7NkW1Q4i3U8Y2OV91htk=/kisspng-computer-icons-youtube-play-button-clip-art-play-button-5ac1d4d25921d5.7177159215226523703651.png) over the image to help people make it obvious it's a clickable link to a video. I'll probably use [Pillow](https://pillow.readthedocs.io) for this.

## Built with

### Python

- Validate YouTube URLs
- Get the correct YouTube video ID for the different types of YouTube URLs
- Get the thumnail data from YouTube's API using requests

### Flask

- Templating HTML with Jinja2
- Get URL out of form and send for processing in Python script
- Get results of Python script and put it into HTML

### Javascript

- Fill the input field with the demo link
