import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import src.models.model

VIEWS_PATH = '../views/'

class MainPage(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(VIEWS_PATH), 'index.html')
    articles = src.models.model.Article.all()
    model = {'name': 'man', 'path': path, 'articles': articles, }
    self.response.out.write(template.render(path, model))

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
