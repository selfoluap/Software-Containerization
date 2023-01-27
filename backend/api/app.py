#!flask/bin/python 
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
 
app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'
 
todos = [ 
    { 
        'id': 1, 
        'desc': u'Take care of some errands', 
        'author': u'Paulo'
    }, 
    { 
        'id': 2, 
        'desc': u'Setting up the project', 
        'author': u'German',  
    } 
] 


@app.route('/', methods=['GET'])
def get_home(): 
    return "Todos App"
 
@app.route('/server/get_task', methods=['GET'])
def get_todo(): 
    return jsonify({'todo': todos[0]})

@app.route('/server/get_tasks', methods=['GET'])
def get_todos(): 
    return jsonify({'todos': todos}) 
 
if __name__ == '__main__': 
    app.run(debug=True)