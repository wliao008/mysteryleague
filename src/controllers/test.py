from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import models.model

class Test(webapp.RequestHandler):
    def get(self):
        create()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Test')
        self.response.out.write('<p>Created')


class TestUser(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('test user: ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
class TestReview(webapp.RequestHandler):
    def get(self):
        article = db.get('agl0dWlsaWNsdWJyCwsSBEl0ZW0YkQMM')
        user = db.get('agl0dWlsaWNsdWJyEAsSBFVzZXIiBuS5kOmYsww')
        for i in range(4):
            review1 = models.model.Review()
            review1.subject="review " + str(i)
            review1.content_html="this is a review " + str(i)
            review1.item = article
            review1.user = user
            review1.put();
        
        self.response.out.write('review created')
        

app = webapp.WSGIApplication([('/test/*', Test), ('/testuser/*', TestUser), ('/testreview/*', TestReview)], debug=True)

def create():
    title = "Test title"
    author = "wliao"
    summary = "this is a test"
    content = "this is the content of the article"
    usr = models.model.User(email="wliao008@gmail.com",nickname="wliao")
    usr.put()
    article = models.model.Article(item_type=1,title=title, original_author=author,summary=summary, content_html=content, user=usr)

    article.put()    

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
