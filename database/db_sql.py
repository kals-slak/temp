from database.queries import *
import datetime
import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(os.environ["DB_URL"])
if conn!=None:
    print("\nDB Connected Successfully!")

today=datetime.date.today()

def createTable():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_TASK_TABLE)

def putOne(name, date, status):
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(INSERT_TASK, (name, date, status))
                print("\nData inserted Successfully!\n")
            except:
                print("\nEnter valid date!\n")

def getOne(task_id):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_ONE, (task_id, ))
            return cursor.fetchone()


def getAll():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_ALL_TASKS)
            return cursor.fetchall()

def getOver():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_COMPLETED)
            return cursor.fetchall()

def getInProgress():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_IN_PROGRESS)
            return cursor.fetchall()

def getFuture():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_FUTURE_TASKS)
            return cursor.fetchall()

def getSorted():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_SORTED)
            return cursor.fetchall()

def getDeadlineExceed():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_DEADLINE_TASK, (today, ))
            return (cursor.fetchall(), today)

def getByDate(date):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_BY_DATE, (today, date))
            return cursor.fetchall()

def delOne(task_id):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(DELETE_ONE, (task_id, ))

def delAll():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(DROP_TABLE)
            