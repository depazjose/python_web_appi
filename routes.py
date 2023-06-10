from datetime import datetime
from flask import Flask, render_template, request


app = Flask(__name__, template_folder = "application/templates")


@app.route('/')
def home():
    return render_template("home.html", today = datetime.now())


@app.route('/about')
def about():
    return 'About!'


@app.route('/news')
def news():
    return 'News!'


@app.route('/your-url', methods =['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        return render_template("your_url.html", code=request.form['code'])
    else:
        return 'This is not valid!'
        
