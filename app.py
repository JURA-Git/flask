import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', active_page='home')

@app.route("/news")
def news():
    return render_template('news.html', active_page='news')

@app.route("/contact")
def contact():
    return render_template('contact.html', active_page='contact')

@app.route("/about")
def about():
    return render_template('about.html', active_page='about')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')