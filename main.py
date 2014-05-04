#The main routing module
import webapp2
from views import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create', CreateHandler),
    ('/edit', EditHandler)
], debug=True)
