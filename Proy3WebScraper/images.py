# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:36:57 2018

@author: AlbertoTP
"""

from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    print ("Search Images")
    search = input ("Search for:")
    params={"q":search}
    dir_name=search.replace(" ", "_").lower()
    
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    
    r=requests.get("https://www.bing.com/images/search", params=params)
    
    soup=BeautifulSoup(r.text, "html.parser")
    links=soup.findAll("a",{"class": "thumb"})
    
    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print ("Getting ",item.attrs["href"])
            tittle=item.attrs["href"].split("/")[-1]
            try:
                img=Image.open(BytesIO(img_obj.content))
                img.save("./"+dir_name+"/"+tittle,img.format)
            except:
                print ("Could not save image")
        except:
            print ("Could not request image")
        
    StartSearch()
    
StartSearch()