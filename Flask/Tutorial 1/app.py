from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/') # path of file
def index():
    return "<h1>Hello, World!</h1>"
# Get method is the default method in Flask.
# To test get: curl http://127.0.0.1:5000/hello (in cmd)
# To test post: curl -X POST http://127.0.0.1:5000/hello
# For the response pattern (HEAD request): curl -I http://127.0.0.1:5000/hello

@app.route('/hello', methods = ['GET', 'POST']) # Access using http://192.168.29.189:5000/hello
def index2():
    if request.method == 'GET' or request.method == 'HEAD':
        return 'You made a GET Request\n', 404 # 404 error code it will show when you use -I (HEAD method)
    elif request.method == 'POST':
        return 'You made a POST Request\n'
    else:
        return 'You will never see this message'

@app.route('/hello/<name>') # Access using http://192.168.29.189:5000/hello/Dev
def greet_name(name):
    return f"Hello, {name}" # will show Hello, Dev
    return "Hello, {}".format(name) # Same as above

# If format is not correct, Not found error will show.
@app.route('/add/<int:num1>/<int:num2>') # http://192.168.29.189:5000/add/15/25
def add(num1, num2):
    return f"Sum is {num1 + num2}" # Output: Sum is 40

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return str(request.args)+ "<br>"+ f"{greeting} {name}!"
    else:
        return "Some parameters missing."

#URL:
# http://192.168.29.189:5000/handle_url_params?name=dev&greeting=hello
# Output:
# ImmutableMultiDict([('name', 'dev'), ('greeting', 'hello')])
# hello dev!

@app.route('/response')
def custom_response():
    response = make_response('Hello World\n')
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return response

# IN CMD
# curl -I http://127.0.0.1:5000/response

# Output:
# HTTP/1.1 202 ACCEPTED
# Server: Werkzeug/3.0.1 Python/3.9.6
# Date: Sun, 26 Apr 2026 13:02:04 GMT
# content-type: application/octet-stream
# Content-Length: 12
# Connection: close

if __name__ == "__main__":
    # Default host is 127.0.0.1 which is localhost (only for machine) but 0.0.0.0 will make it visible for all devices on the network
    # Port = 5000 is the default port for flask web development
    # With debug = True, the server will automatically reload when you make changes to the code, and it will also provide detailed error messages in the browser if something goes wrong.
    app.run(host = '0.0.0.0', port = 5000, debug = True)