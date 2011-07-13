from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template
from google.appengine.api import users, memcache
import models.model
import os
import paging
import hashlib

VIEWS_PATH = os.path.join(os.path.dirname(__file__), '../views/')
PAGE_SIZE = 10

class Setting(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            path = os.path.join(os.path.dirname(VIEWS_PATH), 'setting.html')
            model = {'user': user}
            self.response.out.write(template.render(path, model))
        else:
            #login_url = "/login?continue=" + self.request.uri
            memcache.add(key="return_url", value=self.request.uri, time=300)
            login_url = "/login?continue=/user/authenticate"
            self.redirect(login_url)

class NewAccount(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'new_account.html')
        user = users.get_current_user()
        model = {'user': user}
        self.response.out.write(template.render(path, model))

class Authenticate(webapp.RequestHandler):
    def get(self):
        server = os.environ.get('SERVER_SOFTWARE', '')
        user = users.get_current_user()
        claimed_id = None

        if server.startswith('Dev'):
            claimed_id = 'dev'
        else:
            claimed_id = user.federated_identity()

        if user:# and user.federated_identity():
            #check local db
            #openid = db.Query(models.model.OpenID).filter('claimed_identifier =', 'test')#user.federated_identity())
            query = db.GqlQuery('SELECT * FROM OpenID WHERE claimed_identifier = :1', claimed_id)
            openid = query.fetch(1)
            if openid:
                return_url = memcache.get("return_url")
                #self.response.out.write('federated_identity: ' + claimed_id + ' | ')
                #self.response.out.write('return_url: ' + return_url  + ' | ')
                #self.response.out.write(user.nickname() + ' exists | ')
                #self.response.out.write('openid: ' + openid.claimed_identifier)
                memcache.add('user', openid[0].user)
                memcache.delete('return_url')
                #self.response.out.write('openid[0].user: ' + openid[0].user.nickname)
                self.redirect(return_url)
            else:
                self.response.out.write(user.nickname() + ' DOES NOT exists')
                if server.startswith('Dev'):
                    CreateDevUser(user)
                else:
                    path = os.path.join(os.path.dirname(VIEWS_PATH), 'new_account.html')
                    model={'user': user}
                    self.response.out.write(template.render(path, model))
        else:
            self.response.out.write('Unable to get user obj')

class Register(webapp.RequestHandler):
    def post(self):
        CreateUser(self)
        return_url = memcache.get("return_url")
        if return_url:
            self.redirect(return_url)
        else:
            self.redirect('/')

class UserIndex(webapp.RequestHandler):
    def get(self, key, pagenum=None):
        if pagenum == None:
            pagenum = 0
        user = db.get(key)
        path = os.path.join(os.path.dirname(VIEWS_PATH), 'index_user.html')
        items = models.model.Item.all().filter('user =', user)
        offset = PAGE_SIZE * int(pagenum)
        count = items.count()
        links = paging.link(pagenum, count/PAGE_SIZE, 6, 2, 'prev', 'next', dummy)
        model = {'user': user, 'path': path, "count": count, "page_size": PAGE_SIZE, 'items': items.fetch(PAGE_SIZE, offset), 'links': links}
        self.response.out.write(template.render(path, model))

def CreateUser(self):
    usr = models.model.User()
    usr.nickname = self.request.get('nickname')
    usr.email = self.request.get('email')
    usr.gravatar_icon_url = GetGravatar(usr.email)
    usr.put()
    memcache.add('user', usr)

    openid = models.model.OpenID()
    openid.claimed_identifier = self.request.get('federated_identity')
    openid.friendly_identifier = self.request.get('federated_provider')
    openid.user = usr
    openid.put()

def CreateDevUser(self):
    usr = models.model.User()
    usr.nickname = 'dev'
    usr.email = 'mysterybbs@gmail.com'
    usr.gravatar_icon_url = GetGravatar(usr.email)
    usr.put()

    openid = models.model.OpenID()
    openid.claimed_identifier = 'dev'
    openid.friendly_identifier = 'dev.com'
    openid.user = usr
    openid.put()
    memcache.add('user', usr)

def GetGravatar(email):
    g = 'http://www.gravatar.com/avatar/%(hash)s?d=identicon&s=32'
    if email:
        m = hashlib.md5()
        m.update(email)
        return g % {'hash': m.hexdigest()}
    else:
        return g % {'hash': '00000000000000000000000000000000'}


def dummy():
    print 'dummy'
