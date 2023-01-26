import os
import sqlalchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

engine = sqlalchemy.create_engine(os.environ.get('DB_URL'))
metadata = sqlalchemy.MetaData()

# # init psycopg2
# # conn = psycopg2.connect(
# #     database = os.environ.get("POSTGRES_DB"),
# #     user=os.environ.get("POSTGRES_USER"),
# #     password=os.environ.get("POSTGRES_PASSWORD"),
# #     host="localhost"
# # )

conn = engine.connect()
tasksTable = sqlalchemy.Table('tasksTable', metadata,
                              sqlalchemy.Column('taskID', sqlalchemy.String),
                              sqlalchemy.Column('timeStart', sqlalchemy.Time),
                              sqlalchemy.Column('timeEnd', sqlalchemy.Time),
                              sqlalchemy.Column('date', sqlalchemy.Date),
                              )


def init():
    exist = sqlalchemy.inspect(engine).has_table("tasksTable")
    if exist == False:
        print("=Table doesn't exist=")
        metadata.create_all(engine)
        print("=Table was created=")
        return ("<p> done boy</p>")
    else:
        return ("<p>data up to date</p>")

# def print_tasks_week():
#   return 0


def create_task(_taskID, _taskDate, _startingTime, _endingTime):
    insrt = (
        tasksTable.insert().
        values(taskID=_taskID, date=_taskDate,
               timeStart=_startingTime, timeEnd=_endingTime)
    )
    conn.execute(insrt)
    return ("<p>inserted successfully</p>")


def update_task(taskID_old, taskID_new, taskDate_new, startingTime_new, endingTime_new):
    stmt = tasksTable.update().where(tasksTable.c.taskID == taskID_old).values(
        taskID=taskID_new, date=taskDate_new, timeStart=startingTime_new,
        timeEnd=endingTime_new
        )
    conn.execute(stmt)
    return ("<p> task updated</p>")


def remove_task(_taskID):
    stmt = tasksTable.delete().where(tasksTable.c.taskID == _taskID)
    conn.execute(stmt)
    return ("<p>removed successfully</p>")
