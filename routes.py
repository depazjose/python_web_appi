from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import json

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
        urls = {}
        urls[request.form['code']] = {'url':request.form['code']}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template("your_url.html", code=request.form['code'])
    else:
        return redirect('/')


