from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # Not really required for text and password as they are sent as empty strings.
        if "username" in request.form.keys() and "password" in request.form.keys(): 
            username = request.form['username']
            password = request.form.get('password')

            if username == 'dev' and password == 'pass':
                return "Success"
            else:
                return "Failure"
        return ""
    else:
        return ""

@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
    return 

@app.route('/convert_csv', methods=['GET','POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype = "text/csv",
        headers = {
            'Content-Disposition' : 'attachment; filename = result.csv'
        }
    )
    return response

@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))
    return render_template('download.html', filename = filename)

@app.route('/download/<filename>')
def download(filename):
    # send_from_directory is a Flask function that sends a file from a given directory. It takes the directory name, the filename, and an optional download_name parameter that specifies the name of the file when downloaded.
    return send_from_directory('downloads', filename, download_name = 'result.csv')

@app.route('/handle_post', methods = ['POST'])
def handle_post():
    greetings = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greetings}, {name}')

    return jsonify({'message': 'Successfully written!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)