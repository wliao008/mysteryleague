from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import src.models.model

class Test(webapp.RequestHandler):

  def get(self):
    create()
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Test')
    self.response.out.write('<p>Created')


app = webapp.WSGIApplication([('/test/*', Test)], debug=True)

def create():
  article = src.models.model.Article(title="Test title", author="wliao")
  article.summary = "this is a test"
  article.content = "this is the content of the article"
  article.put()    

def main():
  run_wsgi_app(app)

if __name__ == "__main__":
  main()
