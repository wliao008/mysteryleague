from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
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
            login_url = "/login?continue=" + self.request.uri
            self.redirect(login_url)
