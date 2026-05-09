from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'Dev'
    myresult = 10 + 20
    mylist = [10, 20, 30]
    return render_template('index.html', value = myvalue, result = myresult, list1 = mylist)

@app.route('/random_url')
def filter():
    some_text = "Hello, World!"
    return render_template('filter.html', some_text = some_text)

@app.route('/redirect')
def redirect_to_filter():
    return redirect('/random_url')
    return redirect(url_for('filter')) # same thing.

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, n = 2):
    return s * n

@app.template_filter('alternate_case')
def alternate(s):
    return ''.join([c.upper() if i%2 == 0 else c.lower() for i, c in enumerate(s)])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)