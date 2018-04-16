 
import web

urls = (
  '/', 'hello',
  '/bye/', 'bye')

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('templates/', base='base')

class hello:
    def GET(self):
        return render.hello("Templates demo", "Hello", "A long time ago...")

class bye:
    def GET(self):
        return render.bye("Templates demo", "Bye", "14", "8", "25", "42", "19")

if __name__ == "__main__":
    app.run()