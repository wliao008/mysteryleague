from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Item(polymodel.PolyModel):
  title = db.StringProperty(required=True)

class Article(Item):
  author = db.StringProperty()
