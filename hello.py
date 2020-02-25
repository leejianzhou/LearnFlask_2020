from flask import Flask, request, render_template, jsonify
from flask import make_response, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return 'Hello World！!'

@app.route('/login')
def login():
    session['logged_in'] = True  #写入session
    return redirect(url_for('hello'))

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','Human')
    response = '<h0>Hello, %s</hs>' % name
    #下面，将根据用户认证状态(是否执行/login)返回不同的内容
    if 'logged_in' in session:
        response += '[授权]'
    else:
        response += '[未授权]'

    return response

@app.route('/hi', methods=['GET', 'POST'])
def say_hello():
    return render_template('hi_request.html')


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name='Peter'):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/getrequest')
def getrequest():
    ##以http://127.0.0.1:8080/getrequest?name=Grey
    name=request.args.get('name','Flask')
    return '<h1>Hello, %s!<h1>' % name

@app.route('/goback/<int:year>')
def go_back(year):
    return '<p> 出生年：%d </p>' % (2020-year)

colors = ['blue', 'white', 'black']

@app.route('/colors/<any(%s):color>' % str(colors)[1:-1])
def three_colors(color):
    return '<p>You select the color is %s. ' % color

@app.route('/foo')
def foo():
    response = make_response('<h1>Hello, text/plain</h1>')
    #response.mimetype = 'text/plain'
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route('/foo2')
def foo2():
    data = {
        'name': 'Grey Li',
        'gender': 'male'
    }
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response

@app.route('/foo3')
def foo3():
    return jsonify(name='Grey Li', gender='male', age='30')

if __name__ == '__main__':
    app.run()
