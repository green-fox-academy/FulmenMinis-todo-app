import sys 
import os

class Todo(object):

    def __init__(self):
        os.system("clear")
        
    def controller(self):
        self.arguments = [
            {"argument": "-l", "description": "Lists all the tasks"},
            {"argument": "-a", "description": "Adds new task"},
            {"argument": "-r", "description": "Removes a task"},
            {"argument": "-c", "description": "Completes a task"}
        ]
        if len(sys.argv) == 1:
            print ("\n Command Line Todo application \n ============================= " + 
            "\n Command line arguments: \n  -l   Lists all the tasks \n  -a   " + 
            "Adds a new task \n  -r   Removes an task \n  -c   Completes an task")
        elif len(sys.argv) == 2 and sys.argv[1] == "-l":
            return self.list_todo()
        elif len(sys.argv) == 3 and sys.argv[1] == "-a":
            item = str(sys.argv[2])
            return self.add_todo(item)
        elif len(sys.argv) == 3 and sys.argv[1] == "-r":
            index = int(sys.argv[2])
            return self.remove_item(index)
        elif len(sys.argv) == 3 and sys.argv[1] == "-c":
            index = int(sys.argv[2])
            return self.check_item(index)
        else: 
            print("Unable to add: no task provided")
    
    def list_todo(self):
        try:
            file = open("todo_list.txt") 
            lines = [line.rstrip('\n') for line in open('todo_list.txt')] #rstrip
            index_num = 1
            file.close()
            if len(lines) == 0:
                print("There are no todos for today :)")
            else:
                for i in lines:
                    print(index_num, i)
                    index_num += 1    
        except FileNotFoundError:
            return 0
    
    def add_todo(self, item):
        try:
            file = open("todo_list.txt", "a")
            file.write(str("\n" + "[ ] " + item))
            file.close()
        except IOError:
            print("Unable to write file.")

    def remove_item(self, index):
        try:
            with open("todo_list.txt","r") as textfile:
                listed = list(textfile)
                del listed[index - 1]    
            with open("todo_list.txt","w") as textfile:
                for n in listed:
                    textfile.write(n)    
        except IOError:
            print("Unable to write file.")

    def check_item(self, index):
        try:
            tasks = open("todo_list.txt", "r")
            line = tasks.readlines()
            complete = int(sys.argv[2]) - 1
            tasks.close()
            if int(sys.argv[2]) > len(line):
                return print("Unable to check: index is out of bound")
            tasks = open("todo_list.txt", "w")
            for i in range(len(line)):
                if line[i][0:3] == "[ ]" and i == complete:
                    tasks.write("[x]" + line[i][3:])
                else:
                    tasks.write(line[i])
            tasks.close()
        except FileNotFoundError:
            return 0
        
app = Todo()
app.controller()
