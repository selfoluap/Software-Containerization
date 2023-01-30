# #!flask/bin/python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
db.init_app(app)

class Todo(db.Model):
  __tablename__ = 'TodoTable'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), unique=False, nullable=False)
  description = db.Column(db.String(150), unique=False, nullable=False)

  def __init__(self, title, description):
    self.title = title
    self.description = description

db.create_all()

@app.route('/server/todos', methods=['GET'])
@cross_origin() 
def get_todos(): 
    todos = TodoTable.query.all()
    return jsonify(todos)


@app.route("/server/todos", methods=['POST'])
@cross_origin()
def create_todo_server():
    body = request.get_json()
    db.session.add(Todo(body['title'], body['description']))
    db.session.commit()
    return "todo successfully created"

    
@app.route("/server/todos/<id>", methods=['DELETE'])
@cross_origin()
def remove_todo_server(id):
    db.session.query(Todo).filter_by(id=id).delete()
    db.session.commit()
    return "todo successfully deleted"

 
if __name__ == '__main__': 
    app.run(debug=True) 
