# Samantha Ngo
# Softdev -- pd7
# hw13
# 2017-11-09

from flask import Flask, render_template, request
import urllib2, json
from util import album

app = Flask(__name__)

# NASA API
nasa = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=hnMJycsr0ttvB0vkB7NqgGwp1X5z2bHmviBia3DC")
landslides = urllib2.urlopen("https://data.nasa.gov/resource/tfkf-kniw.json")

# test = content.info()
nasa_info = nasa.read()
nasa_data = json.loads(nasa_info)
    
@app.route('/')
def launch():
    # NASA API
    image1 = nasa_data["hdurl"]
    explanation = nasa_data["explanation"]

    return render_template('launch.html', image1 = image1, explanation = explanation)

@app.route("/radio", methods=['GET','POST'])
def radio():
    # Last.fm API
    artist = request.form.get("artist")
    print artist
    cd = request.form.get("album")
    print cd
    
    try:
        summary = album.getInfo(artist, cd)
    except:
        summary = "We couldn't find your requested artist and/or album"
    return render_template("radio.html", summary=summary)

if __name__ == "__main__":
    app.debug = True
    app.run()
