from flask import Flask
import os



application = Flask(__name__)


def get_banner_js():
    classification = os.environ.get('CLASSIFICATION', 'TOP SECRET')
    banner_color = os.environ.get('BANNER_COLOR', '#f0ad4e')
    js = '''
    (function() {
      setTimeout(function () {

        // Header
        var banner = document.createElement("div");
        banner.className = "classification-banner";
        banner.innerHTML = "{0}";
        banner.style = "display: block; background-color: {1}; color: #fff; font-weight: bold; text-align: center; text-shadow: 1px 1px 0 #444; margin-left: -2rem; position: absolute; width: 98.5vw; height: 16px"

        var content = document.getElementsByClassName("navbar-pf-vertical")[0];
        if (typeof(content) != 'undefined' && content != null)
        {
          content.insertBefore(banner, content.firstChild);
        } else {
          var body = document.body;
          body.insertBefore(banner, body.firstChild);
        }

        // Footer
        var bannerFooter = document.createElement("footer");
        bannerFooter.className = "classification-banner-footer";
        bannerFooter.innerHTML = {0};
        bannerFooter.style = "display: block; background-color: {1}; color: #fff; font-weight: bold; text-align: center; text-shadow: 1px 1px 0 #444; position: absolute; width: 98.5vw; bottom: 0; z-index: 99999; height: 16px"
        var body = document.body;
        body.appendChild(bannerFooter);

      }, 1000);
    }());'''.format(classification, banner_color)
    return js


@application.route("/")
def hello():
    return get_banner_js()

if __name__ == "__main__":
    application.run()
