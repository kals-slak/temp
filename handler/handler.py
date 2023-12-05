from database.db_sql import *
from datetime import datetime, date

createTable()

def addNew():
    name=input("Enter the task: ")
    date=input("Enter deadline for task YYYY-MM-DD: ")
    status=input("Enter the status of task 0(Completed) / 1(In Progress) / 2(Yet to): ")

    if name and date and status in ('0','1','2'):
        putOne(name, date, status)
    else:
        print("\nEnter Valid Status!\n")
        addNew()
        return

def viewOne():
    id_ip=input("Enter the task id: ")
    task=getOne(id_ip)
    if len(task)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_STATUS\n", sep="\t\t\t")
        status=task[3]
        status="Completed" if status==0 else("In Progress" if status==1 else "Yet to")
        print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ",  status)
    else:
        print("\nThere task id don't match any task!\n")

def viewAll():
    tasks=getAll()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_STATUS\n", sep="\t\t\t")
        for task in tasks:
            status=task[3]
            status="Completed" if status==0 else("In Progress" if status==1 else "Yet to")
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ",  status)
    else:
        print("\nThere is no task currently in the DB!\n")

def viewCompleted():
    tasks=getOver()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_COMPLETED", "TASK_DEADLINE\n", sep="\t\t\t")
        for task in tasks:
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ")
    else:
        print("\nThere is no completed task currently!\n")

def viewInProgress():
    tasks=getInProgress()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_IN_PROGRESS", "TASK_DEADLINE\n", sep="\t\t\t")
        for task in tasks:
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ")
    else:
        print("\nThere is no task in progress currently!\n")

def viewFuture():
    tasks=getFuture()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_YET_TO", "TASK_DEADLINE\n", sep="\t\t\t")
        for task in tasks:
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ")
    else:
        print("\nThere is future assigned task currently!\n")

def viewSorted():
    tasks=getSorted()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_STATUS\n", sep="\t\t\t")
        for task in tasks:
            status=task[3]
            status="Completed" if status==0 else("In Progress" if status==1 else "Yet to")
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ",  status)
    else:
        print("\nThere is no task currently in the DB!\n")

def viewDeadBeyond():
    tasks, today=getDeadlineExceed()
    # today=datetime
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_OVERRUN_BY (in days)", "TASK_STATUS\n", sep="\t\t\t")
        for task in tasks:
            status=task[3]
            status="In Progress" if status==1 else "Yet to"
            print("  ", task[0], "\t\t ", task[1], "\t\t\t", task[2],"\t\t\t  ", str(today-task[2]).split(",")[0],"\t\t\t",  status)
    else:
        print("\nThere is no task beyond deadline!\n")

def viewByDate():
    user_date=input("Enter deadline date limit YYYY-MM-DD: ")
    user_date=datetime.strptime(user_date, "%Y-%m-%d").date()
    if user_date < date.today():
        print("Date must be greater than or equal to today!")
        return

    tasks=getByDate(user_date)
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_STATUS\n", sep="\t\t\t")
        for task in tasks:
            status=task[3]
            status="Completed" if status==0 else("In Progress" if status==1 else "Yet to")
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ",  status)
    else:
        print("\nThere is no task currently in the DB!\n")

def removeTask():
    id_ip=input("Enter the task id to delete: ")
    confirm=input("Are you sure you want to delete the task ? (y/n)")
    if confirm in ('y', 'Y'):
        delOne(id_ip)
        print("Task deleted successfully!")
    else:
        print("Delete operation cancelled!")

def removeAll():
    confirm=input("Are you sure you want to remove all tasks ? (y/n): ")
    if confirm in ('y','Y'):
        delAll()
        print("All Task deleted successfully!")
    else:
        print("Delete operation cancelled!")
