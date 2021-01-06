import sys
from datetime import date
if ( len(sys.argv) == 1 or (sys.argv[1] == 'help' and len(sys.argv) == 2)) :
  string_variable = "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics\n"
  sys.stdout.buffer.write(string_variable.encode('utf8')) 
elif (sys.argv[1] == 'ls' and len(sys.argv) == 2):
        fp = open("todo_task.txt")
        count = len(open('todo_task.txt').readlines(  ))
        if count == 0:
           print('There are no pending todos!') 
        else:   
            Lines = fp.readlines() 
            for line in Lines: 
                string_variable = "[{}]: {}".format(count, line.strip())+'\n'
                sys.stdout.buffer.write(string_variable.encode('utf8'))
                count -= 1
elif (sys.argv[1] == 'add' ):
      if (len(sys.argv) == 2):
          string_variable = 'Error: Missing todo string. Nothing added!'
          sys.stdout.buffer.write(string_variable.encode('utf8'))
      else: 
         f = open("todo_task.txt",'r')
         file = f.readlines()
         file.insert(0,sys.argv[2]+'\n')
         f.close()
         f = open("todo_task.txt", "w")
         f.writelines(file)
         f.close()
         print('Added todo: "'+sys.argv[2]+'"' )
elif (sys.argv[1] == 'del' ):
    if (len(sys.argv) == 2):
          string_variable = 'Error: Missing NUMBER for deleting todo.'
          sys.stdout.buffer.write(string_variable.encode('utf8')) 
    else:  
        count = len(open('todo_task.txt').readlines(  ))
        if(count >= int(sys.argv[2]) and int(sys.argv[2]) > 0):
            todo = open('todo_task.txt')
            lines = todo.readlines()
            todo.close()
            line = lines[count - int(sys.argv[2])] 
            del lines[count - int(sys.argv[2])] 
            f = open("todo_task.txt", "w")
            f.writelines(lines)
            f.close()
            string_variable = "Deleted todo #"+sys.argv[2]
            sys.stdout.buffer.write(string_variable.encode('utf8')) 
        else:
          string_variable = 'Error: todo #'+sys.argv[2]+' does not exist. Nothing deleted.'
          sys.stdout.buffer.write(string_variable.encode('utf8'))           
elif (sys.argv[1] == 'done'):
    if (len(sys.argv) == 2):
          string_variable = 'Error: Missing NUMBER for marking todo as done.'
          sys.stdout.buffer.write(string_variable.encode('utf8')) 
    else:  
        count = 0
        count = len(open('todo_task.txt').readlines(  ))
        if(count >= int(sys.argv[2]) and int(sys.argv[2]) > 0):
            todo = open('todo_task.txt')
            lines = todo.readlines()
            todo.close()
            line = lines[count - int(sys.argv[2])] 
            del lines[count - int(sys.argv[2])] 
            f = open("todo_task.txt", "w")
            f.writelines(lines)
            f.close()
            string_variable = "Marked todo #"+sys.argv[2]+" as done."
            sys.stdout.buffer.write(string_variable.encode('utf8')) 
            f = open("done_task.txt",'r')
            file = f.readlines()
            file.insert(0,'x '+str(date.today())+' '+line)
            f.close()
            f = open("done_task.txt", "w")
            f.writelines(file)
            f.close()
        else:
          string_variable = 'Error: todo #0 does not exist.'  
          sys.stdout.buffer.write(string_variable.encode('utf8'))         
elif (sys.argv[1] == 'report' and len(sys.argv) == 2):
    string_variable = str(date.today())+' Pending : '+ str(len(open('todo_task.txt').readlines(  )))+' Completed : '+str(len(open('done_task.txt').readlines(  )))
    sys.stdout.buffer.write(string_variable.encode('utf8')) 
else: 
  print("command not found")  