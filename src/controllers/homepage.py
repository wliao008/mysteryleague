from google.appengine.ext import db, webapp
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
        model = {'name': 'man', 'path': path, 'articles': articles.fetch(PAGE_SIZE, offset), }
        count = articles.count()
        self.response.out.write(count)
        self.response.out.write(template.render(path, model))

class ArticleDetail(webapp.RequestHandler):
    def get(self, cat, key):
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'articledetail.html')
        article = db.get(key)
        model = {'cat': cat, 'article': article}
        self.response.out.write(template.render(path, model))


application = webapp.WSGIApplication([('/', MainPage), ('/page(\d+)', MainPage), (r'/(detail)/(\w+)', ArticleDetail)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
