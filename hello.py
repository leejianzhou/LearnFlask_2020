from flask import Flask, request, render_template

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

if __name__ == '__main__':
    app.run()
