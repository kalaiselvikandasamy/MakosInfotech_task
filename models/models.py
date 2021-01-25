from app import db
from datetime import datetime

class Candidates(db.Model):
	__tablename__ = 'candidates'
	id = db.Column(db.Integer,primary_key = True)
	sname = db.Column(db.String(100),nullable = False,default = 'N/A')
	fname = db.Column(db.String(100),nullable = False,default = 'N/A')
	dob = db.Column(db.String(100), nullable = False)
	address = db.Column(db.Text,nullable = False,default = 'N/A')
	city = db.Column(db.String(100),nullable = False,default = 'N/A')
	state = db.Column(db.String(100),nullable = False,default = 'N/A')
	email = db.Column(db.String(100),nullable = False,default = 'N/A', unique=True)
	password = db.Column(db.String(100),nullable = False,default = 'N/A')
	tenthName = db.Column(db.String(100),nullable = False,default = 'N/A')
	tenthScore = db.Column(db.Integer,nullable = False,default = 'N/A')
	twethName = db.Column(db.String(100),nullable = False,default = 'N/A')
	twethScore = db.Column(db.Integer,nullable = False,default = 'N/A')
	ugName = db.Column(db.String(100),nullable = False,default = 'N/A')
	ugScore = db.Column(db.Integer,nullable = False,default = 'N/A')
	collegeId = db.Column(db.LargeBinary, nullable = False)
	working = db.Column(db.String(100),nullable = False,default = 'No')
	company = db.Column(db.String(100),nullable = False,default = 'No Company name')

	def __str__(self):
		return self.id
