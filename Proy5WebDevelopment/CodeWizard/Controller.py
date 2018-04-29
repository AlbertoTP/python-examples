# -*- coding: utf-8 -*-
import web
from Models import RegisterModel,LoginModel,Posts

web.config.debug = False

urls = ('/','home',
        '/discover','discover',
        '/profile','profile',
        '/settings','settings',
        '/login','login',
        '/check-login', 'checkLogin',
        '/logout','logout',
        '/register','register',
        '/postregistration','postregistration',
        '/postActivity', 'postActivity',
        '/hello/', 'hello')

app = web.application(urls, globals(), autoreload=True)
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render('Views/Templates/', base='Home', globals={'session': session_data, 'current_user': session_data["user"]})

#Classes/Routes
class hello:
    def GET(self):
        return render.Hello("Templates demo", "Hello", "A long time ago...")

class home:
    def GET(self):
        #print (self)
        #print (render)
        data = type('obj', (object,),{"username":"beto","password":"beto"})
        log=LoginModel.LoginModel()
        isCorrect=log.check_user(data)
        if isCorrect:
            session_data['user'] = isCorrect
            
        post_model=Posts.Posts()
        posts=post_model.get_all_posts()

            #print (posts)
        return render.MainLayout(posts)
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
        
class login:
    def GET(self):
        return render.Login()
        
class checkLogin:
    def POST(self):
        data = web.input()
        print ("data is (post) ",data)
        log=LoginModel.LoginModel()
        isCorrect=log.check_user(data)
        if isCorrect:
            session_data['user'] = isCorrect
            return isCorrect
        return "error"
        
        
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
        
class logout:
    def GET(self):
        session['user']=None
        session_data['user']=None
        
        #session.kill()
        return "success"
        
class postActivity:
    def POST(self):
        data = web.input()
        data.username=session_data['user']['username']
        
        post_model=Posts.Posts()
        new_post=post_model.insert_post(data)
        return 'success'
        
if __name__ == "__main__":
    app.run()