from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import models.model
import os

VIEWS_PATH = '../views/'
PAGE_SIZE = 50

class MainPage(webapp.RequestHandler):
    def get(self, pagenum=None):
        if pagenum == None:
            pagenum = 0
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'index.html')
        articles = models.model.Article.all()
        articles.order("-created_date")
        offset = PAGE_SIZE * int(pagenum)
        count = articles.count()
        model = {'name': 'man', 'path': path, "count": count, "page_size": PAGE_SIZE, 'articles': articles.fetch(PAGE_SIZE, offset), }
        self.response.out.write(template.render(path, model))

class Login(webapp.RequestHandler):
    def get(self):
	path = os.path.join(os.path.dirname(VIEWS_PATH), 'login.html')
	self.response.out.write(template.render(path, None))

application = webapp.WSGIApplication([
				('/', MainPage), 
				('/page(\d+)', MainPage),
				('/login', Login)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
