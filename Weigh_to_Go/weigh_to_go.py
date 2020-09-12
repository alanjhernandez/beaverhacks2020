from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, WeightForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'feabff93bfc17d29f4a3f4196c3473c8'

@app.route('/')
@app.route('/home')
def home():
	#methods=['GET','POST']
	#form = WeightForm()
	#if form.validate_on_submit():
		#flash(f'Entered a weight','success')
		#return redirect(url_for('answer'))
	#return render_template('home.html', title = 'Home', form=form)
	return render_template('home.html',  title = 'Home')
#^This routes the user to the home page as the default

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')
#^This routes the user to the about page when they add /about to the url

@app.route('/register', methods=['GET','POST'])
# Allows user to access the register page, POST allows us
# to send info to a web server, GET is used to retrieve info from
# a web server
def register():
	form = RegistrationForm()
	form.validate()
	# object code is found in forms.py
	if form.validate_on_submit():
		# form validates, alert user 
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
# Allows user to access login form
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/answer', methods=["POST"])
# Shows plates needed for specific weight
def answer():
	weights = {"45 lb": 0, "35 lb": 0, "25 lb": 0, "10 lb": 0, "5 lb": 0, "2.5 lb": 0}
	plates = request.form.get("plates")
	title = "Your Plates"
	weight = (int(plates) - 45.0)/2.0
    
	if weight%1 != 0:
		weight = weight - 2.5
		weights["2.5 lb"] =+ 1

	if weight >= 45.0:
		num45 = weight//45
		weight = weight - (num45 * 45.0)
		weights["45 lb"] =+ int(num45)

	if weight >= 35.0:
		num35 = weight//35
		weight = weight - (num35 * 35.0)
		weights["35 lb"] =+ int(num35)

	if weight >= 25.0:
		num25 = weight//25
		weight = weight - (num25 * 25.0)
		weights["25 lb"] =+ int(num25)

	if weight >= 10.0:
		num10 = weight//10
		weight = weight - (num10 * 10.0)
		weights["10 lb"] =+ int(num10)

	if weight >= 5.0:
		num5 = weight//5
		weight = weight - (num5 * 5.0)
		weights["5 lb"] =+ int(num5)

	return render_template("/answer.html", title=title, weights=weights)


if __name__== '__main__':
	app.run(debug=True)
    
