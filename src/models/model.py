from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Status(db.Model):
    status_name = db.StringProperty(required=True)

class User(db.Model):
    email = db.StringProperty()
    nickname = db.StringProperty()
    gravatar_icon_url = db.LinkProperty()
    created_date = db.DateTimeProperty(auto_now_add=True) 

class OpenID(db.Model):
    claimed_identifier = db.StringProperty()
    friendly_identifier = db.StringProperty()
    login_count = db.IntegerProperty(default=0)
    created_date = db.DateTimeProperty(auto_now_add=True)
    user = db.ReferenceProperty(User, collection_name='openids')

class Item(polymodel.PolyModel):
    title = db.StringProperty(required=True)
    item_type = db.IntegerProperty(required=True)
    summary = db.StringProperty()
    content_html = db.TextProperty()
    content_wmd = db.TextProperty()
    created_date = db.DateTimeProperty(auto_now_add=True)
    hits = db.IntegerProperty(default=0)
    is_reviewable = db.BooleanProperty(default=True)
    is_ratable = db.BooleanProperty(default=True)
    rating = db.RatingProperty()
    icon_url = db.StringProperty()
    user = db.ReferenceProperty(User)
    status = db.ReferenceProperty(Status)

class Article(Item):
    original_author = db.StringProperty()

class Book(Item):
    isbn = db.StringProperty()
    sub_title = db.StringProperty()
    original_title = db.StringProperty()
    price = db.FloatProperty(default=None)
    published_year = db.IntegerProperty(default=None)
    published_month = db.IntegerProperty(default=None)
    published_day = db.IntegerProperty(default=None)
    page_count = db.IntegerProperty(default=None)
    

class Review(db.Model):
    item = db.ReferenceProperty(Item, collection_name='reviews')
    subject = db.StringProperty()
    content_html = db.TextProperty()
    content_wmd = db.TextProperty()
    ip_address = db.StringProperty()
    created_date = db.DateTimeProperty(auto_now_add=True)
    user = db.ReferenceProperty(User)
    rating = db.RatingProperty()
    up_vote = db.IntegerProperty(default=0)
    down_vote = db.IntegerProperty(default=0)
