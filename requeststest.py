# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:57:56 2018

@author: AlbertoTP
"""

import  requests

#save HTML
print ("\n\nExample Get HTML and search a word\n")
params={"q": "pizza"}
r = requests.get("https://www.bing.com/search", params=params)
print ("Status: ",r.status_code)
print ("URL:")
print (r.url)
#print ("TEXT:")
#print (r.text)

f=(open("./page.html", "+w"))
f.write(r.text)



#Save Image
print ("\n\nExample GET Image\n")
from io import BytesIO
from PIL import Image

r = requests.get("http://kb4images.com/images/epic-wallpaper/36957308-epic-wallpaper.jpg")
print ("Status code:", r.status_code)

image=Image.open(BytesIO(r.content))

print (image.size, image.format, image.mode)
path="./image."+image.format

try:
    image.save(path, image.format)
except IOError:
    print ("Cannot save image.")
    


#Post
print ("\n\nExample Post Metod\n")
my_data={"name": "Alberto", "email":"alberto.tapia.p@gmail.com"}
r=requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

#f=open("myfile.html","+w")
#f.write(r.text)
print(r.text)


#Posting JSON
print ("\n\nExample Post JSON\n")
import simplejson as json
url="https://www.googleapis.com/urlshortener/v1/url"
payload={"longUrl:":"http://example.com/"}
headers={"Content-Type":"application/json"}
r=requests.post(url, json=payload)

print(json.loads(r.text)["error"]["code"])
print (r.text)

print (r.headers)