from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
import os
import cgi
import models.model

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')

class ItemDetail(webapp.RequestHandler):
    def get(self, item_type, key):
	item_template = ''
	book = None
	item = None
	if item_type == '1':
		item_template = 'articledetail.html'
	elif item_type == '2':
		item_template = 'bookdetail.html'
	elif item_type == '3':
		item_template = 'persondetail.html'

        path = os.path.join(os.path.dirname(VIEWS_PATH), item_template)
        item = db.get(key)
        item.hits += 1
        item.put()
        user = users.get_current_user()
        login_url = ""
        login_msg = ""
        if not user:
		#login_url = users.create_login_url(self.request.uri)
		login_url = "/login?continue=" + self.request.uri
		login_msg = "Please <a href=" +  login_url + ">login</a> to leave comment ;)"

        model = {'book': book, 'item': item, 'user': user, 'login_url': login_url, 'login_msg': login_msg}
        self.response.out.write(template.render(path, model))

    def post(self):
        #TODO: shouldn't retrieve the whole article object just to reference it,
        #there should be a better way, research on how the foreign key work in appengine
        key = self.request.get('key')
        article = db.get(key)
        review = model.Review()
        review.content_html = cgi.escape(self.request.get('content'))
        review.item = article
        review.put()
        self.redirect("/detail/" + key)