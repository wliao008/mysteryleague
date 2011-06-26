from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template
from google.appengine.api import users, memcache
import models.model
import os

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')

class Setting(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            path = os.path.join(os.path.dirname(VIEWS_PATH), 'setting.html')
            model = {'user': user}
            self.response.out.write(template.render(path, model))
        else:
            #login_url = "/login?continue=" + self.request.uri
	    memcache.add(key="return_url", value=self.request.uri, time=300)
	    login_url = "/login?continue=/user/authenticate"
            self.redirect(login_url)

class NewAccount(webapp.RequestHandler):
    def get(self):
	path = os.path.join(os.path.dirname(VIEWS_PATH), 'new_account.html')
	model = {'user': user}
	self.response.out.write(template.render(path, model))

class Authenticate(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
	if user and user.federated_identity():
	    #check local db
	    openid = db.Query(models.model.OpenID).filter('claimed_identifier =', user.federated_identity())
	    if openid:
	        self.response.out.write('federated_identity: ' + user.federated_identity() + ' | ')
	        data = memcache.get("return_url")
		self.response.out.write('return_url: ' + data + ' | ')
		self.response.out.write(user.nickname() + ' exists')
	    else:
		self.response.out.write(user.nickname() + ' DOES NOT exists')
	else:
	    self.response.out.write('Unable to get user obj')
