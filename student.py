while True:
  print("===== Student Record System =====\n\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit")

  val = int(input("enter your choice:"))

#enter new student detail
  if val == 1:
    name = input("Name  :")
    age = input("age   :")
    course =input("course:")
    detail = name+","+age+","+course+"\n"
    with open("detail.txt","a") as file:
        file.write(detail)

#show student detail code
  elif val == 2:
    with open("detail.txt","r") as file:
        lines=file.readlines()        
        for line in lines:
            line = line.strip()
            lst = line.split(",")
            
            print(lst[0]+" | "+lst[1]+" | "+lst[2])
#show search student
  elif val==3:
      name = input("Enter student name:")
      with open("detail.txt","r") as file:
          lines = file.readlines()
          for line in lines:
              line = line.strip()
              line = line.split(",")
              if line[0].lower() == name.lower():
                  print(f"NAME:{line[0]} | AGE:{line[1]} | COURSE:{line[2]}")
                  
  elif val == 4:
      name = input("Enter student name:")
      ind = 0
      with open("detail.txt","r") as file:
          lines = file.readlines()
          for line in lines:
              
              line = line.split(",")
              if line[0].lower() == name.lower():
                  break
                  
                  
                 
                
  elif val == 5:
    print("PROGRAM IS EXITED")
    break
  else:
      print("ENTER NUMBER BETWEEN 1 - 5")
    

