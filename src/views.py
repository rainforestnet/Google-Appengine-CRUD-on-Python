#Collection of handlers which is to process route request from main.py

import webapp2
import cgi
import jinja2
import os

from datetime import datetime
from logics import Employee
from google.appengine.ext import db
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

jinja_environment.globals['year'] = datetime.now().year

class MainHandler(webapp2.RequestHandler):
    def get(self):
        emp = Employee() 
        template_values = {'employees' : emp.list_employee()}
        template = jinja_environment.get_template('template/index.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.POST.get('delete'): #if user clicks "Delete" button
                employee_ids = self.request.get('employee_id',allow_multiple=True) #allow_multiple=True so that it reads multiple key into list.
                emp = Employee()
                emp.delete_employee(employee_ids)
                self.redirect('/')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = jinja_environment.get_template('template/create.html')
            self.response.out.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        #get all input values
        input_first_name = self.request.get('first_name').strip()
        input_last_name = self.request.get('last_name').strip()
        input_marital_status = self.request.get('marital_status').strip()
        input_gender = self.request.get('gender').strip()
        input_date_of_birth = self.request.get('date_of_birth').strip()
        
        emp = Employee()
        emp.save_employee(input_first_name,input_last_name,input_marital_status,input_gender,input_date_of_birth,0)
        self.redirect('/create')


class EditHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            #get ID of entity Key
            emp_k = db.Key.from_path('CompanyModel','Bellucci','EmployeeModel',long(self.request.get('id')))
            #get entity from key instance
            emp = db.get(emp_k)
            
            template_values = {'employee' : emp}
            template = jinja_environment.get_template('template/edit.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        #get all input values
        input_id = self.request.get('id')
        input_first_name = self.request.get('first_name').strip()
        input_last_name = self.request.get('last_name').strip()
        input_marital_status = self.request.get('marital_status').strip()
        input_gender = self.request.get('gender').strip()
        input_date_of_birth = self.request.get('date_of_birth').strip()

        emp = Employee()
        emp.save_employee (input_first_name,input_last_name,input_marital_status,input_gender,input_date_of_birth,long(input_id))
        self.redirect('/')