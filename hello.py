from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return render_template('hi_request.html')


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name='Peter'):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
