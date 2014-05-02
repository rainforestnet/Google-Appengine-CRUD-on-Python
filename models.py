from google.appengine.ext import db

class EmployeeModel (db.Model):
	timestamp = db.DateTimeProperty(auto_now=True)
	first_name = db.StringProperty()
	last_name = db.StringProperty()
	marital_status = db.StringProperty()
	gender = db.StringProperty()
	date_of_birth = db.DateProperty()
	user_name = db.StringProperty()

class CompanyModel (db.Model):
	name = db.StringProperty()