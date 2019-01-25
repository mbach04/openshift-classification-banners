from flask import Flask
from flask import render_template
import os



app = Flask(__name__)


@app.route("/")
def banner():
    # default to highest class
    # Other common values:
    # SECRET: #FF0000
    # CONFIDENTIAL: #286090
    # UNCLASSIFIED: #5cb85c
    classification = os.environ.get('CLASSIFICATION', 'TOP SECRET')
    banner_color = os.environ.get('BANNER_COLOR', '#f0ad4e')
    return render_template('banner.html', banner_color=banner_color, classification=classification)

if __name__ == "__main__":
    app.run()