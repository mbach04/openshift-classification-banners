(function() {
    setTimeout(function () {
    var i = 0;
      var banner = document.createElement("div");
      banner.className = "classification-banner";
      banner.innerHTML = "{{ classification }}";
      banner.style = "display: block; background-color: {{ banner_color }}; color: #fff; font-weight: bold; text-align: center; text-shadow: 1px 1px 0 #444; position: absolute; left: 0; right: 0; width: 100%; height: 16px"
      var content = document.getElementsByClassName("navbar-pf-vertical")[0];
      if (typeof(content) != 'undefined' && content != null)
      {
        content.insertBefore(banner, content.firstChild);
      } else {
        var body = document.body;
        body.insertBefore(banner, body.firstChild);
      }
      var bannerFooter = document.createElement("footer");
      bannerFooter.className = "classification-banner-footer";
      bannerFooter.innerHTML = "{{ classification }}";
      bannerFooter.style = "display: block; background-color: {{ banner_color }}; color: #fff; font-weight: bold; text-align: center; text-shadow: 1px 1px 0 #444; position: fixed; width: 100%; bottom: 0; z-index: 99999; height: 16px"
      var body = document.body;
      body.appendChild(bannerFooter);
    }, 1000);
  }());
