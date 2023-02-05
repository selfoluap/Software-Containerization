# #!flask/bin/python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS, cross_origin

load_dotenv(find_dotenv())

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
db.init_app(app)
cors = CORS(app, origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'


class Todo(db.Model):
  __tablename__ = 'TodoTable'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), unique=False, nullable=False)
  description = db.Column(db.String(150), unique=False, nullable=False)

  def __init__(self, title, description):
    self.title = title
    self.description = description


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
@cross_origin()
def default():
    return "API for Todos"


@app.route('/server/get_todos', methods=['GET'])
@cross_origin()
def get_todos():
    query_result = db.session.query(Todo).all()
    todos = []
    for todo in query_result:
        todos.append({
            "title": todo.title,
            "description": todo.description,
            "id": todo.id
        })
    return jsonify(todos)


@app.route("/server/create_todo", methods=['POST'])
@cross_origin()
def create_todo_server():
    body = request.get_json()
    todo = Todo(body['title'], body['description'])
    db.session.add(todo)
    db.session.commit()
    return {"msg": "Todo created successfully", 
            "id":  todo.id,
            "status": 201}

    
@app.route("/server/delete_todo/<id>", methods=['DELETE'])
@cross_origin()
def remove_todo_server(id):
    db.session.query(Todo).filter_by(id=id).delete()
    db.session.commit()
    return {"msg": "Todo deleted successfully",
            "status": 200}


if __name__ == '__main__': 
    app.run(debug=True) 
 
