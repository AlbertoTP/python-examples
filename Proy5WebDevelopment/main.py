# -*- coding: utf-8 -*-

import web

urls = {
    '/(.*)',"index"
}

app=web.application(urls, globals())

class index:
    def GET(self, name):
        print ("Hello ", name ," How are you today?")
        return "<h1>Hello "+ name +"</h1><br> How are you today?"

if __name__== "__main__":
    app.run()