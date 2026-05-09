from flask import render_template, request, redirect

from models import Person

def register_routes(app, db):
    
    @app.route('/', methods=['GET','POST'])
    def index():
        # if request.method == 'GET':
        if request.method == 'POST':
            name = request.form.get('name')
            age = request.form.get('age')
            job = request.form.get('job')
            person = Person(name=name, age=age, job=job)
            db.session.add(person)
            db.session.commit()
            # REDIRECT here so a refresh triggers a GET request, not a POST
            return redirect('/')
        people = Person.query.all()
        return render_template('index.html', people = people)
    
    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        people = Person.query.all()
        return render_template('index.html', people = people)
    
    @app.route('/details/<pid>', methods=['GET'])
    def details(pid):
        person1 = Person.query.filter(Person.pid == pid).first()
        return render_template('details.html', person = person1)