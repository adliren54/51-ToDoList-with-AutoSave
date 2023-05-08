import os, time
print("To Do List Manager")
todo = []

f = open("todo.txt", "r")
todo = eval(f.read())
f.close()

def prettyPrint():
  print("To Do List") 
  print()
  for index in range(len(todo)):
    print(f"{index + 1}: {todo[index]}") 

while True:
  menu = input("Do you want to add, edit, or remove an item from the to do list?\n")
  if menu == "add":
    task = input("To Do > ")
    if task in todo:
      print("The task you add is already on the list")
    else:
      todo.append(task)
  elif menu == "remove":
    task = input("What do you want to remove?\n")
    if task in todo:
      check = input("Are you sure you want to remove this?\n")
      if check == "yes":
        todo.remove(task)
      elif check == "no":
        continue
    else:
      print("Task is not in your To Do List")
  elif menu == "view":
    prettyPrint()
  elif menu == "edit":
    item = input("What do you want to change?\n")
    new = input("What do you want to change into?\n")
    for i in range(0, len(todo)):
      if todo[i] == item:
        todo[i] = new
  elif menu == "delete":
    check = input("Are you sure you want to delete list?\n")
    if check == "yes":
      todo = []
    else:
      continue
  time.sleep(1)
  os.system('clear')

  f = open("todo.txt", "w")
  f.write(str(todo))
  f.close()