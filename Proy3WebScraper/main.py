# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:42:31 2018

@author: AlbertoTP
"""

from bs4 import BeautifulSoup
import requests
print ("Search with BeautifulSoup")
search = input("Enter search: ")
print()
params={"q":search}
r=requests.get("https://www.bing.com/search", params=params)

soup=BeautifulSoup(r.text, "html.parser")
results=soup.find("ol",{"id":"b_results"})
links=results.findAll("li",{"class":"b_algo"})

for item in links:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]
    
    if item_text and item_href:
        print(item_text)
        print(item_href)
        print(item.get_text())
        print ("\n")