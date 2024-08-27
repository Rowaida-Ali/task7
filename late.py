a,b=0,1
n=int(input("enter a number "))
fib=[]
for i in range(n+1):
    fib.append(a)
    a,b=b,a+b
print(fib[n-1])    


dict=[]
s=input("enter your name")
def check_name():
    if i  not in dict:
        dict.append(s) 
sender=input("what you want to send")
reciver=input("reciver")
message1=input("msg")        
def send_msg(send,recive,msg):
        message={
            "sender":send,
            "reciver":recive,
            "message":msg,
        } 
        dict.append(message)
        print(message)
send_msg(sender,reciver,message1)
def show_msg():
    name=input("enter name you are checking for ")
    if name in dict and name==sender and name==reciver:
        print(dict)
show_msg()        
      
print(dict)
tasks=[]
def add_task(add):
    tasks.append(add)
def removed_task(removed):
    if removed not in tasks:
        print("not found") 
    else:
        tasks.remove(removed) 
        print(f"task {removed} has been removed ")  
def completed_tasks(completed):
    if completed not in tasks:
        print("not found")
    else:
        print(f"your task  {completed}  is done")    
           
while True:
    options=input("add,remove,view_all,mark as done")
    if options=="add":
        add=input("what you want to add:")
        add_task(add) 
        print(f"task has been added succesfully {tasks} ")
    if options=="remove":
        removed=input("what you want to remove:")
        removed_task(removed)
    if options=="view all":
        print("all your list is here ",tasks)  
    if options=="completed tasks":
        completed=input("what has been finished ")
        completed_tasks(completed)                               
   