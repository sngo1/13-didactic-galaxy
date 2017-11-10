# Samantha Ngo
# Softdev -- pd7
# hw13
# 2017-11-09

from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)
content = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=hnMJycsr0ttvB0vkB7NqgGwp1X5z2bHmviBia3DC")
landslides = urllib2.urlopen("https://data.nasa.gov/resource/tfkf-kniw.json")

# test = content.info()
info = content.read()
data = json.loads(info)
    
@app.route('/')
def launch():
    image1 = data["hdurl"]
    explanation = data["explanation"]
    
    return render_template('launch.html', image1 = image1, explanation = explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()
