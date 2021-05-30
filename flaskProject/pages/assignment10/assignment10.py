from flask import Flask, render_template, redirect, url_for, request, session, Blueprint
import mysql.connector

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')


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


@assignment10.route("/assignment10")
def usersList():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route("/assignment10insert", methods=['GET', 'POST'])
def insert_user():
    name = request.form['name']
    nickname = request.form['nickname']
    query = "insert into users(user_nickname, user_name) values ('%s', '%s')" % (nickname, name)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


@assignment10.route("/assignment10update", methods=['POST'])
def update_user():
    name = request.form['name']
    nickname = request.form['nickname']
    query = "update users set user_name = '%s' where user_nickname='%s';" % (name, nickname)
    interact_db(query, query_type='commit')
    return redirect("/assignment10")

@assignment10.route("/assignment10delete", methods=['POST'])
def delete_user():
    nickname = request.form['nickname']
    query = "delete from users where user_nickname='%s';" % (nickname)
    interact_db(query, query_type='commit')
    return redirect("/assignment10")




