from django.utils import simplejson
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os
from google.appengine.ext import db

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')

class Test(webapp.RequestHandler):
    def get(self):
        model = {}
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'test.html')
        self.response.out.write(template.render(path, model))

class Testajax(webapp.RequestHandler):
    def get(self):
        term = self.request.get("term")
        query = db.GqlQuery("SELECT * FROM Tag WHERE name >= :1 AND name < :2", term, term + u"\ufffd")
        result = query.fetch(20, 0)
        data = []
        for x in result:
            data.append(x.name)
        #count = len(result)
        #model = {'msg': str(count)}
        self.response.out.write(simplejson.dumps(data))
