from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from controllers import *

urls = [
	(r'/', MainPage), 
	(r'/page(\d+)', MainPage),
	(r'/login', Login),
	(r'/_ah/login_required', Login),
	(r'/logout', Logout),
	(r'/detail/(\d)-(\w+)', ItemDetail),
	(r'/item/addreview', ItemDetail),
	(r'/testuser', TestUser),
	(r'/setting', Setting),
	# more url patterns
]

application = webapp.WSGIApplication(urls, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
