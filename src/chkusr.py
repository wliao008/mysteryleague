from google.appengine.ext import webapp, db
from google.appengine.api import users
import os

register = webapp.template.create_template_register()

def curr_user():
    server = os.environ.get('SERVER_SOFTWARE', '')
    user = users.get_current_user()
    if user:
	claimed_id = None
	if server.startswith('Dev'):
	    claimed_id = 'dev'
	else:
	    claimed_id = user.federated_identity()

	query = db.GqlQuery('SELECT * FROM OpenID WHERE claimed_identifier = :1', claimed_id)
	openid = query.fetch(1)
	if openid:
    	    return '<a href="/user/setting">' + user.nickname() + '</a> [<a href="/logout">logout</a>]'
	else:
	    return '<a href="/login">login</a>'
    else:
	return '<a href="/login">login</a>'

def ver():
    return os.environ['CURRENT_VERSION_ID']


register.simple_tag(curr_user)
register.simple_tag(ver)
