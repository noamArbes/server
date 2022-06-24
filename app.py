from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

import mysql.connector
import time
import requests
import asyncio
import aiohttp



app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1000)

@app.route('/')
def index_func():
    return render_template('homePage.html')

@app.route('/contact')
def contact_func():
    return render_template('contactUs.html')



@app.route('/about')
def about_func():
    return render_template('assignment3_1.html')
catalog_dict = {
'Rose': {'price': 10, 'color': 'red', 'size': 'Medium'},
'Sunflower': {'price': 15, 'color': 'Yellow', 'size': 'Large'},
'Lilac': {'price': 20, 'color': 'Purple', 'size': 'Medium'},
'Lily': {'price': 10, 'color': 'White', 'size': 'Small'},
'Tulip': {'price': 15, 'color': 'Red/Pink', 'size': 'Medium'},
'Orchid': {'price': 100, 'color': 'Purple/White', 'size': 'Large'}

}


@app.route('/catalog')
def catalog_func():
    if 'flower_name' in request.args:
        flower_name = request.args['flower_name']
        if flower_name in catalog_dict:
            return render_template('assignment3_1.html',
                                   flower_name=flower_name,
                                   flower_price=catalog_dict[flower_name]['price'],
                                   flower_color=catalog_dict[flower_name]['color'],
                                   flower_size=catalog_dict[flower_name]['size'])
        else:
            return render_template('assignment3_1.html',
                                   message='Sorry, flower not found.')
    return render_template('assignment3_1.html',
                           catalog_dict=catalog_dict)



user_dict = {
'Alon95': {'name': 'Alon', 'email': 'alon@gmail.com', 'password': '1114'},
'Guy21': {'name': 'Guy', 'email': 'guy@gmail.com', 'password': '1112'},
'Dana96': {'name': 'Dana', 'email': 'dana@gmail.com','password': '1113'},
'Noam1': {'name': 'Noam', 'email': 'noam@gmail.com','password': '1111'},
'LiorY': {'name': 'Lior', 'email': 'lior@gmail.com','password': '1115'}
}

#
# logIn_dict = {
#     'Noam1': '1111',
#     'Guy21': '1112',
#     'Dana96': '1113',
#     'Alon95': '1114',
#     'LiorY': '1115'
#
# }
@app.route('/logIn', methods=['GET', 'POST'])
def logIn_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user_dict:
            pas_in_dict = user_dict[username]['password']
            if pas_in_dict == password:
                session['username'] = username
                session['logedin'] = True
                return render_template('assignment3_2.html',
                                       username=username
                                       )
            else:
                return render_template('assignment3_2.html',
                                       logIn_message='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   logIn_message='Please Sign In')
    return render_template('assignment3_2.html')


@app.route('/logOut')
def logOut_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('logIn_func'))



@app.route('/user_search')
def user_search_func():
    if 'user_name' in request.args:
        user_name = request.args['user_name']
        if user_name in user_dict:
            return render_template('assignment3_2.html',
                                   user_name=user_name,
                                   name=user_dict[user_name]['name'],
                                   email=user_dict[user_name]['email'])
        elif user_name == '':
            return render_template('assignment3_2.html',
                                   user_dict=user_dict)
        else:
            return render_template('assignment3_2.html',
                                   message='This user does not exist')
    return render_template('assignment3_2.html',
                           user_dict=user_dict)



@app.route('/clear')
def clear_func():
    return redirect(url_for('catalog_func'))

@app.route('/return_toHome')
def returnHome_func():
    return redirect('/')


@app.route('/session')
def session_func():
    return jsonify(dict(session))
