import web

urls = (
   '/', 'index',
   '/me', 'second'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

class second:
    def GET(self):
        call_me = "My name is Sly"
        return call_me

if __name__ == "__main__":
    app.run()
