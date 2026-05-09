from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'SOME KEY'

@app.route('/')
def index():
    return render_template('index.html', message = 'Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello, World'
    return render_template('index.html', message = 'Session data set')

@app.route('/get_data')
def get_data():
    name = session.get('name', 'Not set')
    other = session.get('other', 'Not set')
    return render_template('index.html', message = f'Name: {name}, Other: {other}')

@app.route('/clear_session')
def clear_session():
    session.clear()
    # session.pop('name') # In case you want to remove just some data.  
    return render_template('index.html', message = 'Session data cleared.')


@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message = 'Cookie set'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies.get('cookie_name', None)
    return render_template('index.html', message = f"Cookie value is {cookie_value}")

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message = 'Cookie removed.'))
    response.set_cookie('cookie_name', expires=0) # 0 means Jan 1, 1970 so since the data is in the past, it will delete instantly.
    return response

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Dev' and password == 'pass':
            flash('Successful Login!')
        else:
            flash('Login Failed!')
        return render_template('index.html', message = '')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)