# -*- coding: utf-8 -*-
import web

urls = ('/','home',
        '/discover','discover',
        '/profile','profile',
        '/settings','settings',
        '/register','register',
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
        
class discover:
    def GET(self):
        return render.Discover()
        
class profile:
    def GET(self):
        return render.Profile()
        
class settings:
    def GET(self):
        return render.Settings()
        
class register:
    def GET(self):
        return render.Register()
        
if __name__ == "__main__":
    app.run()