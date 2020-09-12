from flask import Flask, render_template, request
#from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#app.config['SECRET_KEY'] = 'feabff93bfc17d29f4a3f4196c3473c8'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')
#^This routes the user to the home page as the default

@app.route('/about')
def about():
    return render_template('/about.html', title = 'About')
#^This routes the user to the about page when they add /about to the url

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('/register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('/login.html', title='Login', form=form)

@app.route('/answer', methods=["POST"])
def form():
	
	weights = {"45 lb": 0, "35 lb": 0, "25 lb": 0, "10 lb": 0, "5 lb": 0, "2.5 lb": 0}
	plates = request.form.get("plates")
	
	title = "Your Plates"
	
	weight = (int(plates) - 45.0)/2.0
    
	if weight%1 != 0:
		weight = weight-2.5
		weights["2.5 lb"] =+ 1

	if weight >= 45.0:
		weight = weight - 45.0
		weights["45 lb"] =+ 1

	if weight >= 35.0:
		weight = weight - 35.0
		weights["35 lb"] =+ 1

	if weight >= 25.0:
		weight = weight - 25.0
		weights["25 lb"] =+ 1

	if weight >= 10.0:
		weight = weight - 10.0
		weights["10 lb"] =+ 1

	if weight >= 5.0:
		weight = weight - 5.0
		weights["5 lb"] =+ 1

	return render_template("answer.html", title=title, weights=weights)


#if __name__== '__main__':
#	app.run(debug=True)
    
