from flask import Flask, request, render_template
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World！!'


@app.route('/hi')
@app.route('/hello', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run()
