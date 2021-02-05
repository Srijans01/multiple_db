from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:////mnt/c/Users/antho/Documents/multiple_databases/one.db'
app.config['SQLALCHEMY_BINDS'] = {'two' : 'mysqldb::////mnt/c/Users/antho/Documents/multiple_databases/two.db',
                                  'three' : 'mysqldb::////mnt/c/Users/antho/Documents/multiple_databases/three.db'
                                }

db = SQLAlchemy(app)

class One(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Two(db.Model):
    __bind_key__ = 'two'
    id = db.Column(db.Integer, primary_key=True)

class Three(db.Model):
    __bind_key__ = 'three'
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    one = One(id=123)
    db.session.add(one)
    db.session.commit()

    return 'Added a value to the first table!' 

@app.route('/PostgreSQL')
def PostgreSQL():
    second = Two(id=124)
    db.session.add(second)
    db.session.commit()

    return 'Added a value to the second table!' 

@app.route('/MySQL')
def MySQL():
    three = Three(id=125)
    db.session.add(three)
    db.session.commit()

    return 'Added a value to the third table!'


if __name__ == '__main__':
    app.run(debug=True)