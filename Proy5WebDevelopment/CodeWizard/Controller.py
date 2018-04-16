# -*- coding: utf-8 -*-
import web

urls = ('/','home',
        '/hello/', 'hello')

app = web.application(urls, globals(), autoreload=True)
render = web.template.render('Views/Templates/', base='Home')

#Classes/Routes
class hello:
    def GET(self):
        return render.Hello("Templates demo", "Hello", "A long time ago...")

class home:
    def GET(self):
        #print (self)
        #print (render)
        return render.MainLayout()
        #return "<h1> Hello CodeWizards</h1>"
        
if __name__ == "__main__":
    app.run()