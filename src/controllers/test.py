from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from models import model
import os
import markdown

openIdProviders = (
    'Google.com/accounts/o8/id', # shorter alternative: "Gmail.com"
    'Yahoo.com',
    'MySpace.com',
    'AOL.com',
    'MyOpenID.com',
    # add more here
)

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')

class Test(webapp.RequestHandler):
    def get(self):
        create_article()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Test')
        self.response.out.write('<p>Created')


class TestUser(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('Hello <em>%s</em>! [<a href="%s">sign out</a>]' % (
                user.nickname(), users.create_logout_url(self.request.uri)))
        else:
            self.response.out.write('Hello world! Sign in at: ')
            #self.response.out.write('[<a href="%s">%s</a>]' % (users.create_login_url(federated_identity='Yahoo.com', dest_url='/'), 'Yahoo.com'))
            for p in openIdProviders:
                p_name = p.split('.')[0] # take "AOL" from "AOL.com"
                p_url = p.lower()        # "AOL.com" -> "aol.com"
                self.response.out.write('[<a href="%s">%s</a>]' % (users.create_login_url(federated_identity=p_url, dest_url='/'), p_name))
            
class TestReview(webapp.RequestHandler):
    def get(self):
        article = db.get('agl0dWlsaWNsdWJyCwsSBEl0ZW0YkQMM')
        user = db.get('agl0dWlsaWNsdWJyEAsSBFVzZXIiBuS5kOmYsww')
        for i in range(4):
            review1 = model.Review()
            review1.subject="review " + str(i)
            review1.content_html="this is a review " + str(i)
            review1.item = article
            review1.user = user
            review1.put();
        
        self.response.out.write('review created')

class TestWMD(webapp.RequestHandler):
    def get(self):
	wmd = '**hi**'
	ret = markdown.markdown(wmd)
	model = {'wmd': ret}	
	path = os.path.join(os.path.dirname(VIEWS_PATH), 'test.html')
	self.response.out.write(template.render(path, model))

app = webapp.WSGIApplication([('/test/*', Test), ('/testuser/*', TestUser), ('/testreview/*', TestReview)], debug=True)

def create():
    title = "Test title"
    author = "wliao"
    summary = "this is a test"
    content = "this is the content of the article"
    usr = model.User(email="wliao008@gmail.com",nickname="wliao")
    usr.put()
    book = model.Book(item_type=2,title=title, summary=summary, content_html=content, user=usr)
    book.isbn = "123456789"
    
    book.put()    

def create_article():
    title = "Test title - article"
    author = "wliao"
    summary = "this is a test"
    content = "this is the content of the article"
    usr = model.User(email="wliao0082@gmail.com",nickname="wliao2")
    usr.put()
    article = model.Article(item_type=1,title=title, summary=summary, content_html=content, user=usr)
    article.original_author = "wei liao"
    
    article.put()    

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
