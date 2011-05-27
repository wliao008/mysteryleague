from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import models.model

class Test(webapp.RequestHandler):
    def get(self):
        create(100)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Test')
        self.response.out.write('<p>Created')


class TestUser(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('test user: ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp.WSGIApplication([('/test/*', Test), ('/testuser/*', TestUser)], debug=True)

def create(count):
    for i in range(0,count,1):
        title = "Test title " + str(i)
        author = "wliao"
        summary = "this is a test " + str(i)
        content = "this is the content of the article"
        article = models.model.Article(title=title, author=author,
                               summary=summary, content=content)

        article.put()    

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
