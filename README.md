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

* Proy 4 Getting started with pymongo
    * Tools
        * [Install MongoDB (V3.4)](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
        * [Robo 3T](https://robomongo.org/)
    * [MongoDB](https://docs.mongodb.com/)
    * Pymongo
      ```
      pip3 install pymongo
      ```
        * [Documentation](https://api.mongodb.com/python/current/)
        * [Api Documentation](https://api.mongodb.com/python/current/api/)
    * [Query and Projection Operators](https://docs.mongodb.com/manual/reference/operator/query/)
    * [Comparison Query Operators](https://docs.mongodb.com/manual/reference/operator/query-comparison/)


        | Name 	| Description |
        | --- | --- |
        | $eq 	| Matches values that are equal to a specified value.
        | $gt 	| Matches values that are greater than a specified value.
        | $gte 	| Matches values that are greater than or equal to a specified value.
        | $in 	| Matches any of the values specified in an array.
        | $lt 	| Matches values that are less than a specified value.
        | $lte 	| Matches values that are less than or equal to a specified value.
        | $ne 	| Matches all values that are not equal to a specified value.
        | $nin 	| Matches none of the values specified in an array.


    * Making a Connection with MongoClient
    * Getting a Database
    * Getting a Collection
    * Insert documents
    * Getting a Single Document With find_one()
    * Querying By Object
    * Bulk Inserts
    * Indexing

* Proy 5 Web Development project using web.py
    * [Web.py](http://webpy.org/)
      ```
      pip install web.py
      pip install web.py==0.40.dev0
      ```
    * HTML templates
    * Building MVC
    * Import static files
    * Setting up a register form
    * Posting data to web.py
    * Creating users
    * Hashing password
    * Login logic
    * Sessions
    * Logout
    * Posting microblogs
    * Retrieving post objects
    * User settings and updating Mongo
    * Relative datetimes
    * Maling your post dates
    * Adding post comments
    * Images uploads and avatars