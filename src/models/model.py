from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Item(polymodel.PolyModel):
    title = db.StringProperty(required=True)
    summary = db.StringProperty()
    content = db.TextProperty()

class Article(Item):
    author = db.StringProperty()
