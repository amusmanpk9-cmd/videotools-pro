
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>VideoTools Pro</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                background: #101827;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 40px 15px;
            }
            h1 { color: #38bdf8; }
            .tool {
                background: #1e293b;
                padding: 20px;
                margin: 15px auto;
                border-radius: 12px;
                max-width: 400px;
            }
        </style>
    </head>
    <body>
        <h1>VideoTools Pro</h1>
        <p>Your all-in-one video toolbox</p>
        <div class="tool">🎬 Video Converter</div>
        <div class="tool">✂️ Video Cutter</div>
        <div class="tool">🎵 Audio Extractor</div>
        <div class="tool">📦 Video Compressor</div>
        <p>More tools coming soon!</p>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run()
  
