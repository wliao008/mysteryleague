from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Status(db.Model):
    status_name = db.StringProperty(required=True)

class User(db.Model):
    email = db.StringProperty()
    nickname = db.StringProperty()
    gravatar_icon_url = db.LinkProperty()
    created_date = db.DateTimeProperty(auto_now_add=True) 

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
