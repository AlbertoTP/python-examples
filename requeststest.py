# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:57:56 2018

@author: AlbertoTP
"""

import  requests

params={"q": "pizza"}
r = requests.get("https://www.bing.com/search", params=params)
print ("Status: ",r.status_code)
print ("URL:")
print (r.url)
#print ("TEXT:")
#print (r.text)

f=(open("./page.html", "+w"))
f.write(r.text)