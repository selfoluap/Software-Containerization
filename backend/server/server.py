#!flask/bin/python
import Flask
from db import print_tasks_day, print_tasks_week, update_task, remove_task, create_task

app = Flask(__name__)


@app.route("/")
def init():
    return "<p>Good morning beatiful. It is time to get things done hehe </p>"

@app.route("/db/tasks/day", methods=['GET'])
def print_tasks_day():
    return jsonify({'tasks': get_day_tasks()})

@app.route("/db/tasks/week", methods=['GET'])
def print_tasks_week():
    return jsonify({'tasks': get_week_tasks()})

@app.route("/db/task/create", methods=['POST'])
def create_task():
    input = request.get_json() #get input for the task
    taskID = input['taskID']
    taskDate = input['taskDate']
    startingTime = input['timeStart']
    endingTime = input['timeEnd']
    create_task(taskID, taskDate, startingTime, endingTime)
    return "<p> New task! Keep it up. </p>"


@app.route("/task/update", methods=['POST'])
def update_task():
    input = request.get_json() #get input for the task
    taskID = input['taskID']
    taskDate = input['taskDate']
    startingTime = input['timeStart']
    endingTime = input['timeEnd']
    update_task(taskID, taskDate, startingTime, endingTime)
    return "<p> Updated. </p>"

@app.route("/task/remove", methods=['GET'])
def remove_task():
    input = request.get_json() #get input for the task
    taskID = input['taskID']
    taskDate = input['taskDate']
    startingTime = input['timeStart']
    remove_task(taskID, taskDate, startingTime) #assume there cannot be 2 tasks with the same name in parallel
    return "<p>Removed.</p>"



if __name__ == '__main__': 
    app.run(debug=True) 
