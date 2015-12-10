import web

urls = (
   '/', 'Index',
   '/me', 'Second'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

class Second(object):
    def GET(self):
        call_me = "My name is Sly"
        return call_me

if __name__ == "__main__":
    app.run()
