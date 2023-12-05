from handler.handler import *

choice="""

1) Enter a new Task
2) View task by id
3) View all tasks
4) View completed
5) View tasks in progress
6) View future tasks
7) View Sorted task data
8) View task beyond deadline
9) View by date (>= today)
10) Update task status
11) Delete a task 
12) Clean Entire List
q) Exit

"""
def routeReq():
    while (ip:=input(choice))!='q':
        if ip=='1':
            addNew()

        elif ip=='2':
            viewOne()

        elif ip=='3':
            viewAll()

        elif ip=='4':
            viewCompleted()

        elif ip=='5':
            viewInProgress()

        elif ip=='6':
            viewFuture()

        elif ip=="7":
            viewSorted()

        elif ip=='8':
            viewDeadBeyond()
        
        elif ip=='9':
            viewByDate()

        elif ip=='10':
            pass

        elif ip=='11':
            removeTask()

        elif ip=='12':
            removeAll()

        else:
            print("Quiting Unexpected Input!")
            break