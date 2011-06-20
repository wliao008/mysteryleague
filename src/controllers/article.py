from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import os

VIEWS_PATH = '../views/'

class ArticleDetail(webapp.RequestHandler):
    def get(self, cat, key):
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'articledetail.html')
        article = db.get(key)
        article.hits += 1
        article.put()
        user = users.get_current_user();
        login_url = ""
        if not user:
            login_url = users.create_login_url(self.request.uri)
        model = {'cat': cat, 'article': article, 'user': user, 'login_url': login_url}
        self.response.out.write(template.render(path, model))


application = webapp.WSGIApplication([(r'/(detail)/(\w+)', ArticleDetail)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
