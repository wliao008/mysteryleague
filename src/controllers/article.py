from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import os
import cgi
import models.model

VIEWS_PATH = '../views/'

class ArticleDetail(webapp.RequestHandler):
    def get(self, cat, key):
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'articledetail.html')
        article = db.get(key)
        article.hits += 1
        article.put()
        user = users.get_current_user();
        login_url = ""
	login_msg = ""
        if not user:
            login_url = users.create_login_url(self.request.uri)
	    login_msg = "Please <a href=" +  login_url + ">login</a> to leave comment ;)"
        model = {'cat': cat, 'article': article, 'user': user, 'login_url': login_url, 'login_msg': login_msg}
        self.response.out.write(template.render(path, model))

    def post(self):
	key = self.request.get('key')
	article = db.get(key)
        user = users.get_current_user()
	review = models.model.Review()
	review.content_html = cgi.escape(self.request.get('content'))
	review.item = article
	review.put()
	self.redirect("/detail/" + key)

application = webapp.WSGIApplication(
				[(r'/(detail)/(\w+)', ArticleDetail),
				(r'/item/addreview', ArticleDetail)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
