from flask import Flask, render_template, request, session, redirect, jsonify
import mysql.connector
from pages.assignment10.assignment10 import assignment10

app = Flask(__name__)
app.secret_key = '123'

app.register_blueprint(assignment10)

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


@app.route("/assignment11/users")
def assignment11_users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    response = "Table is empty"
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)
    return response


@app.route("/assignment11/users/selected", defaults={'user_id': 123})
@app.route("/assignment11/users/selected/<int:user_id>")
def assignment11_select_user(user_id):
    query = "select * from users where user_id='%s';" % user_id
    query_result = interact_db(query=query, query_type='fetch')
    response = "ID not exist"
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)
    return response


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='ex10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


if __name__ == '__main__':
    app.run(debug=True)