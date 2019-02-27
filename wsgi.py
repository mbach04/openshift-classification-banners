from flask import Flask
from flask import render_template
from flask import Response
import os



application = Flask(__name__)


@application.route("/banner.js")
def banner():
    # default to highest class
    classification = os.environ.get('CLASSIFICATION', 'TOP SECRET')
    if classification.upper() == "TOP SECRET":
        banner_color = '#f0ad4e'
    elif classification.upper() == "CONFIDENTIAL":
        banner_color = '#286090'
    elif classification.upper() == "SECRET":
        banner_color = '#ff0000'
    elif classification.upper() == "UNCLASSIFIED":
        classification = "DYNAMIC CONTENT - HIGHEST POSSIBLE CLASSIFICATION IS: UNCLASSIFIED//FOR OFFICIAL USE ONLY";
        banner_color = '#5cb85c'
    else:
        banner_color = '#ffc0cb'
        classification = "NO CLASSIFICATION SET"
    resp = Response(render_template('banner.js', banner_color=banner_color, classification=classification), status=200, mimetype="application/javascript")
    return resp

if __name__ == "__main__":
    application.run()
