# coding:utf-8

from flask import Flask,request
# Flask是初始化库，request是接受数据并处理库


app = Flask(__name__)
# 初始化一个对象，命名为app


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
            

if __name__ == '__main__':
    app.run()
