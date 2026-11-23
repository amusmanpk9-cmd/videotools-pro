from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/video-converter")
def video_converter():
    return "<h1>Video Converter</h1><p>Coming Soon</p>"

@app.route("/video-to-mp3")
def video_to_mp3():
    return "<h1>Video to MP3</h1><p>Coming Soon</p>"

@app.route("/youtube-downloader")
def youtube_downloader():
    return "<h1>YouTube Downloader</h1><p>Coming Soon</p>"

@app.route("/facebook-downloader")
def facebook_downloader():
    return "<h1>Facebook Downloader</h1><p>Coming Soon</p>"

@app.route("/dailymotion-downloader")
def dailymotion_downloader():
    return "<h1>Dailymotion Downloader</h1><p>Coming Soon</p>"

@app.route("/word-to-pdf")
def word_to_pdf():
    return "<h1>Word to PDF</h1><p>Coming Soon</p>"

@app.route("/pdf-to-word")
def pdf_to_word():
    return "<h1>PDF to Word</h1><p>Coming Soon</p>"
