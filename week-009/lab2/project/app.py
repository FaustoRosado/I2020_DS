import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, request, json

app = Flask(__name__)


url = 'https://www.coalitionforthehomeless.org/basic-facts-about-\
       homelessness-new-york-city-data-and-charts/'


response = requests.get("https://www.coalitionforthehomeless.org/basic-facts-about-\
       homelessness-new-york-city-data-and-charts/")

soup = BeautifulSoup(response.content, 'html.parser')


@app.route('/')
#@app.route('/index/')
def home():
    soup.prettify()
    return render_template('index.html')



@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/user/<username>/')
def page(username):
    print(f"The {username} page!")
    return render_template('user.html', name=username)

@app.route('/info', methods = ["GET", "POST"])
def info():
    req = request
    return render_template("info.html", req=req)
    

if __name__ == '__main__':
    app.run(debug=True)
