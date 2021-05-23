from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = '123'

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


@app.route('/assignment9', methods=["GET", "POST"])
def assignment9():
    curr_method = request.method
    users = {"Bibi123": "Bibi", "Gantz123": "Beni", "Lapid123": "Yair", "Benet123": "Naftul", "Culam0": "Culam"}
    session['user_nickname'] = ''
    user_name = ''
    user_name_src = ''

    if curr_method == "GET":
        if 'user_name_src' in request.args:
            user_name_src = request.args['user_name_src']
        else:
            user_name_src = ''
    elif curr_method == "POST":
        if 'user_name' in request.form:
            user_name = request.form['user_name']
        else:
            user_name = ''
        if user_name in users:
            session['user_nickname'] = users[user_name]
        else:
            session['user_nickname'] = ''
    else:
        user_name, user_name_src = '', ''

    return render_template("assignment9.html",
                           users=users,
                           user_name=user_name,
                           curr_method=curr_method,
                           user_name_src=user_name_src,
                           )


@app.route("/logout")
def logout():
    session['user_nickname'] = ''
    return redirect('/assignment9')



if __name__ == '__main__':
    app.run(debug=True)