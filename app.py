from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

'''
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
'''


if __name__ == '__main__':
    app.run(debug=True)
