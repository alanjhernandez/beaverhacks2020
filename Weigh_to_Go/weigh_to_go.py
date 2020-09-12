from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'feabff93bfc17d29f4a3f4196c3473c8'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')
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
	# object code is found in forms.py
	if form.validate_on_submit():
			# form validates, alert user 
			# flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
# Allows user to access login form
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__== '__main__':
	app.run(debug=True)
    