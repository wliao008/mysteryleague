from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import models.model
import os

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')
PAGE_SIZE = 50

class MainPage(webapp.RequestHandler):
    def get(self, pagenum=None):
        if pagenum == None:
            pagenum = 0
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'index.html')
        articles = models.model.Article.all().filter('item_type =', 1)
        articles.order("-created_date")
        offset = PAGE_SIZE * int(pagenum)
        count = articles.count()
        model = {'name': 'man', 'path': path, "count": count, "page_size": PAGE_SIZE, 'articles': articles.fetch(PAGE_SIZE, offset), }
        self.response.out.write(template.render(path, model))

class Login(webapp.RequestHandler):
    def get(self):
        #user = users.get_current_user()
        action = self.request.get('action')
        target_url = self.request.get('continue')
        if action and action == "verify":
            f = self.request.get('openid_identifier')
            url = users.create_login_url(target_url, federated_identity=f)
            self.redirect(url)
        else:
            self.response.out.write(template.render(VIEWS_PATH + "login.html", \
                {"continue_to": target_url}))

class Logout(webapp.RequestHandler):
    def get(self):
        url = users.create_logout_url("/")
        self.redirect(url)
