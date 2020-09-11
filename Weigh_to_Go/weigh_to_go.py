from flask import Flask, render_template
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

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__== '__main__':
	app.run(debug=True)
    