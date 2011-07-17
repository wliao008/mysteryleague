from google.appengine.ext import db
from google.appengine.api import users
import os

def get_current_openid():    
    server = os.environ.get('SERVER_SOFTWARE', '')
    user = users.get_current_user()
    if user:
        claimed_id = None

        if server.startswith('Dev'):
            claimed_id = 'dev'
        else:
            claimed_id = user.federated_identity()

        query = db.GqlQuery('SELECT * FROM OpenID WHERE claimed_identifier = :1', claimed_id)
        openids = query.fetch(1)
        if openids:
            return openids[0]
        else:
            return None
    else:
        return None