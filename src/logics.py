#Where business logics reside.

from models import EmployeeModel,CompanyModel
import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Employee(object):
	def save_employee (self,first_name,last_name,marital_status,gender,date_of_birth,id):
		#id will be greater than zero when EDIT action is triggered.
		if id>0:
			emp_k = db.Key.from_path('CompanyModel','Bellucci','EmployeeModel',long(id))
			emp = db.get(emp_k)
		else:
			comp = CompanyModel(key_name='Bellucci',name='Bellucci Enterprise')
			comp.put()
			emp = EmployeeModel(parent = comp)

		emp.first_name = first_name
		emp.last_name = last_name
		emp.marital_status = marital_status
		emp.gender = gender
		emp.date_of_birth = datetime.date(year=int(date_of_birth[6:10]), month=int(date_of_birth[3:5]), day=int(date_of_birth[0:2]))
		emp.user_name = users.get_current_user().email()
		emp.put()

	def delete_employee (self, employee_ids):
		if len(employee_ids)>0:
			for employee_id in employee_ids:
				emp_k = db.Key.from_path('CompanyModel','Bellucci','EmployeeModel',long(employee_id))
				emp = db.get(emp_k)
				db.delete(emp_k)

	def list_employee (self):
		comp = db.Key.from_path('CompanyModel','Bellucci')
		employee_query = EmployeeModel.all()
		employee_query.ancestor(comp)
		return employee_query