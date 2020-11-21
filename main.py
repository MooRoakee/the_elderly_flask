# 测试git自动部署
# tst2
from flask import Flask,request
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import class_mapper

import json

from models import *
from constant import *
from sqlalchemy.orm.exc import UnmappedClassError


# flask 初始化
app = Flask(__name__)

# mysql初始化
engine = create_engine(CONNECT_URL)
DB_Session = sessionmaker(bind=engine)
db_session = DB_Session()



@app.route('/')
def page_index():
    
    return "Index Page",200


@app.route('/login')
def page_login():
    username = request.args.get('username')
    password = request.args.get('password')
    try:
        q = db_session.query(User).filter(User.username==username).first()  # db = SQLAlchemy()
        
        q_dict = serialize(q)

        q_dict['result'] = 'success'

        if q_dict['password']==password:

            q_json = jsonify(q_dict)
            return q_json
        else:
            return jsonify(WRONG_PASSWORD)

    except UnmappedClassError:
        return jsonify(NO_SUCH_USER)
    
@app.route('/register')
def page_register():
    username = request.args.get('username')
    password = request.args.get('password')
    try:
        q = db_session.query(User).filter(User.username==username).first()
        if(q==None):
            db_session.execute("insert into user (username,password,numOfDevices)values(%s,%s,%d)" % (username, password,0))
            
            db_session.commit()
            return 'success'
        else:
            return jsonify(USER_EXISTS)

    except:
        db_session.execute("insert into user (username,password,numOfDevices)values(%s,%s,%d)" % (username, password,0))
            
        db_session.commit()
        return 'success'


def serialize(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')