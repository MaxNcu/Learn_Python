# coding:utf-8
from flask import Flask,session,url_for,redirect,render_template
import os
app = Flask(__name__,template_folder=(''),static_folder=('web/static'))
app.config['SRCRET_KEY']=os.urandom(24)

@app.context_processor
def contenx():
    user = 'admins'
    return {'username':user}

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)