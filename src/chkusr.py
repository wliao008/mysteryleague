from google.appengine.ext import webapp
register = webapp.template.create_template_register()

def test_tag():
    return "TEST!"

register.simple_tag(test_tag)
