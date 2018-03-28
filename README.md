# Python Examples

Examples of python

* Proy 1 Calculator:
    * import re
    * re.sub()
    ```{r, engine='python', count_lines}
    num = re.sub(r'abc', '', input)              # Delete pattern abc
    num = re.sub(r'abc', 'def', input)           # Replace pattern abc -> def
    num = re.sub(r'\s+', '\s', input)            # Eliminate duplicate whitespaces
    num = re.sub(r'abc(def)ghi', '\1', input)    # Replace a string with a part of itself
    ```
    * eval()

* Proy 2 Battle Game
    * import
    * classes (POO)
    * Instance varibles
    * colors in text
    * menu
    * Instantiate
    * Adding classes (Magic,Items,Heal and diferents types)
    * Heal Bars
    * Targets to attack
    * delete enemies died

* JSON
    * [simplejson](https://simplejson.readthedocs.io/en/latest/)
    * [os](https://docs.python.org/3/tutorial/stdlib.html)
    ```{r, engine='python', count_lines}
    import simplejson as json
    import os
    ```
* [Pypi](https://pypi.python.org/pypi)

* Request
    * [Requests](http://docs.python-requests.org/en/master/user/quickstart/)
      ```
      pip3 install requests
      ```
    * HTTP GET
    * Pillow the image processing library (PIL)
    * Posting Data
    * Posting JSON
    * Headers
    * [Pillow](https://pillow.readthedocs.io/en/3.0.x/index.html) is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
      ```
      pip3 install pillow
      ```
* Proy 3 Web Scraper
    * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library for pulling data out of HTML and XML files.
      ```
      pip3 install bs4
      ```
    * Parsing BeautifulSoup
    * Directional Navigation
    * Image Scaper
    * Improvement web scaper