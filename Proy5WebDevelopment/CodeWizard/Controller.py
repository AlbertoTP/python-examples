# -*- coding: utf-8 -*-
import web
from Models import RegisterModel
#import RegisterModel

urls = ('/','home',
        '/discover','discover',
        '/profile','profile',
        '/settings','settings',
        '/register','register',
        '/postregistration','postregistration',
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
        
class postregistration:
    def POST(self):
        data = web.input()
        print ("data is (post) ",data)
        reg_model=RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username
        
if __name__ == "__main__":
    app.run()