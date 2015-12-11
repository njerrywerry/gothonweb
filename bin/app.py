import web

urls = (
   '/hello', 'Index',
   '/me', 'Second'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "%s, %s" %(form.greet, form.name)
        return render.index(greeting = greeting)

class Second(object):
    def GET(self):
        call_me = "My name is Sly"
        return render.second(call_me = call_me)

if __name__ == "__main__":
    app.run()
