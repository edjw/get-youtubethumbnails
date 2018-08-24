from flask import render_template, redirect, request, flash
from app import app
from main import get_youtube_thumbnail
from overlay import overlay


@app.route("/")
def index():
    return render_template("index.html", title="Get YouTube Thumbnails")


@app.route("/thumbnails", methods=["GET", "POST"])
def submit():
    if request.form:
        yt_url = request.form.get("url_submit")
        thumbnails_data = get_youtube_thumbnail(yt_url)
    else:
        return redirect("/")

    if thumbnails_data:
        return render_template(
            "thumbnails.html",
            title="Your Youtube Thumbnails",
            thumbnails_data=thumbnails_data, yt_url=yt_url
        )
    else:
        flash("")
        return redirect("/")


@app.route("/overlay", methods=["GET", "POST"])
def overlay_logo():

    image_url = request.form.get("image_submit")
    image = overlay(image_url)
    return redirect(image)
