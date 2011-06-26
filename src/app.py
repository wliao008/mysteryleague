from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import util, template
from controllers import *

urls = [
	(r'/', MainPage), 
	(r'/page(\d+)', MainPage),
	(r'/login', Login),
	(r'/_ah/login_required', Login),
	(r'/user/authenticate', Authenticate),
	(r'/user/register', Register),
	(r'/logout', Logout),
	#item
	(r'/item/(\d)-(\w+)', ItemDetail),
	(r'/item/review/(\d)-(\w+)', ItemReview),
	(r'/item/edit/(\d)-(\w+)', ItemEdit),
	(r'/item/edit/(\d)', ItemEdit),
	(r'/item/review/new', ItemEdit),
	(r'/user/setting', Setting),
	(r'/user/(\w+)/', UserIndex),
	(r'/user/(\w+)/page(\d+)', UserIndex),
	(r'/test', Test),
	(r'/testajax', Testajax),
	(r'/new_account', NewAccount),
	(r'/notfound', Error),
	(r'/.*', Error),
	# more url patterns
]

webapp.template.register_template_library('chkusr')

application = webapp.WSGIApplication(urls, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
