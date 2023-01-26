#!flask/bin/python 
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
 
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
 
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
@cross_origin()
def get_todos(): 
    return jsonify({'todos': todos}) 
 
if __name__ == '__main__': 
    app.run(debug=True)