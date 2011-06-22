from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
import os
import cgi
import models.model

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')

class Setting(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'setting.html')
        self.response.out.write(template.render(path, None))
