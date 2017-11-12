import urllib2, json

def getInfo(artist, album):
    url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=672d94c3ccbe808e96ff25ac7731d86d&artist=" + artist + "&album=" + album + "&format=json"
    info = urllib2.urlopen(url)
    info = info.read()
    info = json.loads(info)
    print info
    retStr = "Artist: " + info["album"]["artist"] + "\n"
    retStr += "Album: " + info["album"]["name"] + "\n"
    retStr += "Summary: " + info["album"]["wiki"]["summary"] + "\n"
    
    return retStr

# print getInfo("Adele", "25")
    
