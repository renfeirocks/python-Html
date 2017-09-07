from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
from file import read, create_survey
import csv
@app.route("/", methods=["GET", "POST"])
def index():
	#Takes in user_name and password from the form in index.html
	#If it fails, it redirects back to login
	if request.method == "POST":
		user_name = (request.form["user_name"])
		password = (request.form["password"])
		return authenticate(user_name, password)
	else:
		return render_template("index.html")

# Create a dictionary and initialize ?admin? as a key with
# value = admin's chosen password
users = {'Username':'Admin',  'Password':'password'}
authentic = False

#Checks the username and password matches the details stored in
#dictionary users
def authenticate(user_name, password):
	"""
	:param user_name: The name of the user
	:param password: Password provided by the user
	"""
	#If login details match, redirect to the survey system home page
	if user_name == users['Username'] and password == users['Password']:
		global authentic
		authentic = True
		return redirect("home")
	#Else redirects back to the login page
	else:
		#add error message i.e. "Wrong username and/or password"
		return redirect("/")

@app.route("/home",methods=["POST","GET"] )
def home():
	#Checks login authentication has successfully occurred to prevent
	#unauthorised access
	if authentic:
		if request.method == 'POST':
			selectedValue = request.form['bt']
			return redirect(url_for(selectedValue))
		else:
			return render_template("home.html")
	else:
		#add error message i.e. "Access Denied: Login required"
		return redirect("/")


@app.route("/pool",methods=["POST","GET"] )
def pool():
	if authentic:
		if request.method == "POST":
			question = request.form["question"]
			a1 = request.form["an1"]
			a2 = request.form["an2"]
			a3 = request.form["an3"]
			a4 = request.form["an4"]
			with open('questions.csv','a') as csv_out:
				writer = csv.writer(csv_out)
				writer.writerow([question, a1, a2, a3, a4])
			return redirect(url_for("showpool"))
		return render_template("pool.html")
	else:
		return redirect("/")


@app.route("/showpool")
def showpool():
	if authentic:
		with open('questions.csv','r') as csv_in:
			reader = csv.reader(csv_in)
			for row in reader:
				user_input.append(row)
		return render_template("showpool.html", all_users=user_input)
	else:
		return redirect ("/")


@app.route("/courseq", methods=['GET', 'POST'])
def courseq():
	courses = read('courses.csv')
	questions = read('questions.csv')
	if authentic:
		if request.method == "POST":
			survey_name = request.form["survey"]
			question = request.form.getlist("question")
			return redirect (url_for('.surveys', survey_name = survey_name, question = question))

		return render_template("select.html", all_questions=questions, all_courses=courses)
	else:
		return redirect("/")


@app.route("/survey")
def surveys():
	if authentic:
		survey_name = request.args['survey_name']
		question  = request.args['question']
		return render_template("survey.html", value = survey_name)

		'''

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))

'''
