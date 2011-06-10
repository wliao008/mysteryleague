from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Item(polymodel.PolyModel):
    title = db.StringProperty(required=True)
    item_type = db.IntegerProperty(required=True)
    summary = db.StringProperty()
    content_html = db.TextProperty()
    content_wmd = db.TextProperty()
    createDate = db.DateTimeProperty(auto_now_add=True)
    hits = db.IntegerProperty(default=0)
    is_reviewable = db.BooleanProperty()
    is_ratable = db.BooleanProperty()
    rating = db.RatingProperty()
    user = db.UserProperty()

class Article(Item):
    original_author = db.StringProperty()
