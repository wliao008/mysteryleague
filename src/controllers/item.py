from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users, memcache
import os
import cgi
import models.model
import html2text
import markdown
import helper.user_helper as user_helper

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

        try:
            item = db.get(key)
            path = os.path.join(os.path.dirname(VIEWS_PATH), item_template)
            item.hits += 1
            item.put()
            #curr_user = users.get_current_user()
            openid = user_helper.get_current_openid()
            login_url = ""
            login_msg = ""
            if not openid:
                #login_url = users.create_login_url(self.request.uri)
                login_url = "/login?continue=" + self.request.uri
                login_msg = "Please <a href=" +  login_url + ">login</a> to leave comment ;)"

            user = memcache.get('user')
            tags = db.get(item.tags)
            tagcount = len(tags)
            model = {'book': book, 'item': item, 'tags': tags, 'tagcount': tagcount, 'curr_user': openid, 'user': user, 'login_url': login_url, 'login_msg': login_msg}
            self.response.out.write(template.render(path, model))
        except db.Error:
            self.error(500)
            self.redirect('/notfound')
            #self.response.out.write('err')


    def post(self, item_type, key):
        user = memcache.get('user')
        article = db.get(key)
        review = models.model.Review()
        review.content_html = cgi.escape(self.request.get('content'))
        review.item = article
        review.user = user
        review.put()
        self.redirect("/item/%(item_type)s-%(key)s" % {'item_type': item_type, 'key': key})

class ItemEdit(webapp.RequestHandler):
    def get(self, item_type, key=None):
        item_template = ''
        item = None
        if item_type == '1':
            item_template = 'articledetailedit.html'
        elif item_type == '2':
            item_template = 'bookdetailedit.html'
        elif item_type == '3':
            item_template = 'persondetailedit.html'
        try:
            if key:
                item = db.get(key)
                if not item.content_wmd:
                    item.content_wmd = html2text.html2text(item.content_html)
            else:
                #TODO: make sure user is logged in first
                curr_user = users.get_current_user()
                if not curr_user:
                    login_url = "/login?continue=" + self.request.uri
                    self.redirect(login_url)
                else:		
                    title = "new"
                    summary = ""
                    usr = memcache.get('user')
                    item = models.model.Article(item_type=int(item_type),title=title, summary=summary, user=usr)
                    item.content_wmd = '**hi**'

                path = os.path.join(os.path.dirname(VIEWS_PATH), item_template)
                model = {'item': item}
                self.response.out.write(template.render(path, model))
        except db.Error:
            self.error(500)
            self.redirect('/notfound')

    def post(self, item_type, key=None):
        title = self.request.get('title')
        content_wmd = self.request.get('content_wmd')
        if key:
            item = db.get(key)	
        else:
            summary = ""
            usr = memcache.get('user')
            item = models.model.Article(item_type=int(item_type),title=title, summary=summary, user=usr)

        item.title = title
        item.content_wmd = content_wmd
        item.content_html = markdown.markdown(content_wmd, output_format='html')
        #self.response.out.write(item.content_html)
        item.put()	
        self.redirect('/')

class ItemReview(webapp.RequestHandler):
    def get(self, item_type, key):
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'review.html')	
        item = db.get(key)
        model = {'item': item}
        self.response.out.write(template.render(path, model))

    def post(self, item_type, key):
        title = self.request.get('title')
        summary = "this is a test"
        content_html = self.request.get('content')
        usr = models.model.User(email="wliao0082@gmail.com",nickname="wliao2")
        usr.put()
        article = models.model.Article(item_type=1,title=title, summary=summary, content_html=content_html, user=usr)
        article.put()
        self.redirect('/item/' + item_type + '-' + key)

