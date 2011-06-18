from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import os

VIEWS_PATH = '../views/'

class ArticleDetail(webapp.RequestHandler):
    def get(self, cat, key):
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'articledetail.html')
        article = db.get(key)
        article.hits += 1
        article.put()
        model = {'cat': cat, 'article': article}
        self.response.out.write(template.render(path, model))


application = webapp.WSGIApplication([(r'/(detail)/(\w+)', ArticleDetail)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
