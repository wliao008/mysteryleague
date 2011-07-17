from google.appengine.ext import webapp
import os
import helper.user_helper as user_helper

register = webapp.template.create_template_register()

def curr_user():
    openid = user_helper.get_current_openid()
    if openid:
        return '<a href="/user/setting">' + (str(openid.user.nickname)) + '</a> [<a href="/logout">logout</a>]'
    else:
        return '<a href="/login">login</a>'

def ver():
    return os.environ['CURRENT_VERSION_ID']


register.simple_tag(curr_user)
register.simple_tag(ver)
