from model import Base, Student
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_student(name, year, finished_lab):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	student_object = Student(
		name=name,
		year=year,
		finished_lab=finished_lab)
	session.add(student_object)
	session.commit()

def query_by_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	student = session.query(Student).filter_by(
		name=name).first()
	return student

def query_all():
	"""
	Print all the students in the database.
	"""
	students = session.query(Student).all()
	return students

def delete_student(name):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(Student).filter_by(
		name=name).delete()
	session.commit()

def update_lab_status(name, finished_lab):
	"""
	Update a student in the database, with 
	whether or not they have finished the lab
	"""
	student_object = session.query(Student).filter_by(
		name=name).first()
	student_object.finished_lab = finished_lab
	session.commit()

def query_by_id(student_id):
    student = session.query(Student).filter_by(
        student_id=student_id).first()
    return student

cap_con = ["B", "D", "F", "G", "J", "K", "L", "M", "N", "P", "R", "S", "Sh", "T", "V", "Z"]
con = ["b", "d", "f", "g", "j", "k", "l", "m", "n", "p", "r", "s", "sh", "t", "v", "z"]
vow = ["a", "e", "o", "i", "u"]

def random_name():
	bloop = random.randint(0,3)
	if bloop == 0:
		return random.choice(cap_con) + random.choice(vow)
	if bloop == 1:
		return random.choice(cap_con) + random.choice(vow) + random.choice(con)
	if bloop == 2:
		return random.choice(cap_con) + random.choice(vow) + random.choice(con) + random.choice(vow)
	else:
		return random.choice(cap_con) + random.choice(vow) + random.choice(con) + random.choice(vow) + random.choice(con)

for i in range(100):
	add_student(random_name(), random.randint(1975,2005), random.choice([True, False]))
