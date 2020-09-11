from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')
#^This routes the user to the home page as the default

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')
#^This routes the user to the about page when they add /about to the url

if __name__== '__main__':
	app.run(debug=True)
    