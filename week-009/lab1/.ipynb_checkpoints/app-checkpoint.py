from flask import Flask, render_template, url_for, request, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sqrt/')
@app.route('/sqrt/<input>/')
def sqrt(input):
    value = (int(input) ** 2)
    return render_template('sqrt.html', val=value)

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
