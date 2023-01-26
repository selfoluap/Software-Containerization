# #!flask/bin/python
from flask import *
# import os
# from db import print_tasks_day, print_tasks_week, update_task, remove_task, create_task, init
from db import init, create_task, update_task, remove_task
# import sqlalchemy
from dotenv import load_dotenv, find_dotenv
import datetime



# load_dotenv(find_dotenv())

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
# db = sqlalchemy(app)




# class Item(db.Model):
#     __tablename__='tasks'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), unique=True, nullable=False)
#     content = db.Column(db.String(120), unique=True, nullable=False)

#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

#
@app.route("/")
def initialize():
    return init();

# @app.route('/', methods=['POST'])
# def my_form_post():
#     taskID = request.form['taskID']
#     taskDate = request.form['taskDate']
#     startingTime = request.form['startingTime']
#     endingTime = request.form['endingTime']
#     # create_task(taskID, taskDate, startingTime, endingTime)
#     return "<p> New task! Keep it up. </p>"
# @app.route("/db/tasks/day", methods=['GET'])
# def print_tasks_day():
#     return jsonify({'tasks': get_day_tasks()})

# @app.route("/db/tasks/week", methods=['GET'])
# def print_tasks_week():
#     return jsonify({'tasks': get_week_tasks()})

@app.route("/server/createTask", methods=['GET','POST'])
def create_task_serv():
    date = datetime.date(2023,5,8)
    timeStart = datetime.time(hour=20, minute=30)
    timeEnd = datetime.time(hour=23, minute=30)
    return create_task('papaya', date, timeStart, timeEnd)


@app.route("/server/updateTask", methods=['GET'])
def update_task_serv():
#     input = request.get_json() #get input for the task
#     taskID = input['taskID']
#     taskDate = input['taskDate']
#     startingTime = input['timeStart']
#     endingTime = input['timeEnd']
    date = datetime.date(2050,5,8)
    timeStart = datetime.time(hour=20, minute=30)
    timeEnd = datetime.time(hour=23, minute=30)
    return update_task("papaya", "papaya_new", date, timeStart, timeEnd)
    

@app.route("/server/removeTask", methods=['GET'])
def remove_task_serv():
    # input = request.get_json() #get input for the task
    # taskID = input['taskID']
    # taskDate = input['taskDate']
    # startingTime = input['timeStart']
    remove_task("papaya_new") #assume there cannot be 2 tasks with the same name in parallel
    return "<p>Removed.</p>"

 
if __name__ == '__main__': 
    app.run(debug=True) 
