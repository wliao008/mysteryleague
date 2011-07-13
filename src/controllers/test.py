from django.utils import simplejson
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')

class Test(webapp.RequestHandler):
    def get(self):
        model = {}
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'test.html')
        self.response.out.write(template.render(path, model))

class Testajax(webapp.RequestHandler):
    def get(self):
        model = {'msg': 'hello ajax'}
        self.response.out.write(simplejson.dumps(model))
