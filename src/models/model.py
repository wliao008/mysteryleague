from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Item(polymodel.PolyModel):
    title = db.StringProperty(required=True)
    summary = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    createDate = db.DateTimeProperty(auto_now_add=True)

class Article(Item):
    author = db.StringProperty()
