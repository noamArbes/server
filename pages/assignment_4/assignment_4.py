
import mysql.connector
import requests
from flask import Blueprint, render_template, request, redirect, session, jsonify


assignment_4 = Blueprint('assignment_4', __name__,
                         static_folder='static',
                         template_folder='templates')


@assignment_4.route('/assignment_4')
def main():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)


def userExist_func(username):
    userExist = False
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    for user in users_list:
        if username == user.username:
            userExist = True
            return userExist
    return userExist


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    id = request.form['id']
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    userExists = userExist_func(username)
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    if userExists == True:
        return render_template('assignment4.html', message_i='This Username Alraedy Exists. Please Try Again',
                               users=users_list)
    if userExists == False:
        if username == '':
            return render_template('assignment4.html', message_i='Please Enter A Unique Username', users=users_list)
        else:
            query = "INSERT INTO users(id, username, name, email, password) VALUES ('%s', '%s','%s', '%s', '%s')" % (
            id, username, name, email, password)
            interact_db(query=query, query_type='commit')
            query = 'select * from users'
            users_list = interact_db(query, query_type='fetch')
            return render_template('assignment4.html', message_i='User Added Successfully', users=users_list)


@assignment_4.route('/update_user', methods=['POST'])
def update_user_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    username1 = request.form['username']
    userExists = userExist_func(username1)
    if not userExists:
        return render_template('assignment4.html', message_i='This user does not exist', users=users_list)
    if userExists:
        for user in users_list:
            if username1 == user.username:
                if request.form['username'] == "":
                    return render_template('assignment4.html', message_i='Please Enter A Username', users=users_list)
                else:
                    if request.form['name'] == "":
                        name = user.name
                    else:
                        name = request.form['name']
                    if request.form['email'] == "":
                        email = user.email
                    else:
                        email = request.form['email']
                    if request.form['password'] == "":
                        password = user.password
                    else:
                        password = request.form['password']
                query = "UPDATE users SET name='%s', email = '%s', password = '%s' where username = '%s'" % (
                 name, email, password, username1)
                interact_db(query=query, query_type='commit')
                return render_template('assignment4.html', message_i='user details updated', users=users_list)




@assignment_4.route('/users', methods=['GET'])
def get_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    users_array = []
    for user in users_list:
        users_array.append({
            'username': user.username,
            'email': user.email,
            'name': user.name
        })
    return jsonify(users_array)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='Arbesfeld@123',
                                         database='flask_db')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# -------------------- DELETE --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    username = request.form['username']
    userExists = userExist_func(username)
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    if id == '':
        return render_template('assignment4.html', message_u='No User Chosen', users=users_list)
    elif userExists == False:
        return render_template('assignment4.html', message_u='No User With This Username', users=users_list)
    else:
        query = "DELETE FROM users WHERE username ='%s';" % username
        interact_db(query, query_type='commit')
        query = 'select * from users'
        users_list = interact_db(query, query_type='fetch')
        return render_template('assignment4.html', message_u='User Deleted', users=users_list)


# ------------------------------------------------- #
# ------------------------------------------------- #
#



async def fetch_url(client_session, url):
    """Fetch the specified URL using the aiohttp session specified."""
    # response = await session.get(url)
    async with client_session.get(url, ssl=False) as resp:
        response = await resp.json()
        return response



@assignment_4.route('/session')
def session_func():
    return jsonify(dict(session))





@assignment_4.route('/outer_source', methods=['GET', 'POST'])
def outer_source():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    user_id = request.form['id']
    result = requests.get('https://reqres.in/api/users/' + user_id)
    return render_template('assignment4.html', user_from_api=result.json()['data'], users=users_list)


@assignment_4.route('/restapi_users/', methods=['GET'])
def get_default_user():
    query = 'select * from users where id=1'
    user = interact_db(query, query_type='fetch')
    return jsonify(user)



@assignment_4.route('/restapi_users/', defaults={'USER_ID': 1})
@assignment_4.route('/restapi_users/<int:USER_ID>')
def get_user(USER_ID):
    query = "select * from users where id='%s'" % USER_ID
    user = interact_db(query, query_type='fetch')
    if user:
        return jsonify(user)
    else:
        return jsonify({
            'error': '404',
            'message': 'User not found!!'
        })


if __name__ == '__main__':
    assignment_4.run(debug=True)
