#ThisVeryBugg
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

@app.route('/user/<user_id>')
def user(user_id):
    user = User.query.get(user_id)
    return '<h1>Hello, {}!</h1>'.format(user.name)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    os.system(name)
    return 'Success'

if __name__ == '__main__':
    db.create
