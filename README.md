# CRUD Google Appengine in Python and Datastore (NoSQL)

## Background
I have been designing, developing, supporting business software applications for years, if not decades. 
It is almost safe to say that, most modern business applications keep their data in SQL Databases. Be it CRM, ERP, Accounting, Payroll, Human Resource and etc.

Just like people only grow older not younger every single day, data of software grow larger every day. 
As data grow, the reading/retrieving of data from SQL database gets slower.

You can do either or combination of below.

* Fine tuning indexes.
* Feed more memory to the server.
* Archive data that can be archivable.
* Redesign or restructure of tables.
* The cost of remedy gets higher as you move down.

I began to ask, why is Google search is not getting slower as data on web not just grow but grow exponentially?

The answer is Google proprietary big table.

The next question of mine was, can I build business application with big table technologies since Google is offering its NoSQL Big table through Google Appengine?

Hence, I gave it a try and here is the proof of concept.

Having said that, I have not developed a full solution with such technologies, simply because of :-

You can design NoSql table like you design SQL table. Instead of normalizing table, 
you de-normalize tables, because some NoSQL like Google Datastore doesn’t support table joining! Full suite of business application often uses tens to hundreds of tables, imagine to de-normalize all those tables?
For serious software development, you need to have a team of programmers sooner or later, 
would I be able to assemble a team that capable of working with NoSQL?

## Business Application running on NoSql?
Is it practical for business/enterprise applications to run on NoSql instead of traditional Sql database? 
I have no answer.

This project is merely to showcase how to use create a very simple CRUD (Create, Read, Update, Delete) application 
with [Google Appengine] (http://cloud.google.com/AppEngine) in Python and NoSQL Datastore.

Front end technologies are [Twitter's Bootstrap 3.3.1] (http://getbootstrap.com/) and [Jinja Template Engine] (http://jinja.pocoo.org/).

If you wish to give it a try, simply go to [employee-crud.appspot.com] (http://employee-crud.appspot.com/) and 
login with your Google account (whether it is @gmail.com or your custom domain under Google Apps for Business).

Feel free to Create, Update and Delete any Employee record as you like it.

I tried to keep the code very simple as this is not for practical use but educational purpose, 
it is to serve a reference for anyone who is new to Google Appengine /NoSQL Datastore and you wonder how to build a simple database application with it. 
