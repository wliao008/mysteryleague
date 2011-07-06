from google.appengine.api import users, memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import models.model
import os
import paging

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')
PAGE_SIZE = 10

class MainPage(webapp.RequestHandler):
    def get(self, pagenum=None):
        if pagenum == None:
            pagenum = 0
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'index.html')
        items = models.model.Item.all()#.filter('item_type =', 1)
        items.order("-created_date")
        offset = PAGE_SIZE * int(pagenum)
        count = items.count()
        links = paging.link(pagenum, count/PAGE_SIZE, 6, 2, 'prev', 'next', dummy)
        model = {'ver': os.environ['CURRENT_VERSION_ID'], 'name': 'man', 'path': path, "count": count, "page_size": PAGE_SIZE, 'items': items.fetch(PAGE_SIZE, offset), 'links': links}
        self.response.out.write(template.render(path, model))

class Login(webapp.RequestHandler):
    def get(self):
        #user = users.get_current_user()
        action = self.request.get('action')
        target_url = self.request.get('continue')
	memcache.add(key="return_url", value=os.environ['HTTP_REFERER'], time=300)
        if action and action == "verify":
            f = self.request.get('openid_identifier')
            url = users.create_login_url(target_url, federated_identity=f)
            self.redirect(url)
        else:
            self.response.out.write(template.render(VIEWS_PATH + "login.html", \
                {"continue_to": "/user/authenticate"}))

class Logout(webapp.RequestHandler):
    def get(self):
        url = users.create_logout_url("/")
        self.redirect(url)

class Error(webapp.RequestHandler):
    def get(self):
	path = os.path.join(os.path.dirname(VIEWS_PATH), 'default_error.html')
	model = {'error_msg': 'error'}
	self.response.out.write(template.render(path, model))

def dummy():
    print 'dummy'
