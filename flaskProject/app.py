from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/cv')
def cv():
    return render_template("cv.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/colleagues')
def colleagues():
    return render_template("colleagues.html")


@app.route('/contact me')
def contact_me():
    return render_template("contact me.html")


@app.route('/contact list')
def contact_list():
    return render_template("contact list.html")


@app.route('/hobbies')
def hobbies():
    DefName = 'Ofir'
    return render_template('assignment8.html', name=DefName, hobbies=['Movies', 'Eating', 'Bla Bla'])


@app.route('/Tips for Movies')
def tips():
    DefName = 'Ofir'
    return render_template('assignment8Block.html', name=DefName, hobbies=['Movies', 'Eating', 'Bla Bla'])


if __name__ == '__main__':
    app.run(debug=True)