from google.appengine.ext import webapp
from google.appengine.api import users

register = webapp.template.create_template_register()

def test_tag():
    return "TEST!"

def curr_user():
    user = users.get_current_user()
    if user:
    	return 'logged in'
    else:
	return 'not logged in'

register.simple_tag(curr_user)
