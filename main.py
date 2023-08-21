d = {}
with open('Data.txt') as file:
    for line in file:
        parts = line.strip().split(",")
        key = parts[0]
        val = ",".join(parts[1:])  # Join the remaining parts to get the value
        d[key] = val
#users functions
def find_user(user, d):#O(n*m) m is the avarge lenth of names  and O(m)is the time complexity for each value  and n is the number of elements in the dictionary (d)
    for value in d.values():
        if user.lower() == value.split(',')[0].lower():# split items evey , and get user which is already at index 0
            return True
    return False
def find_id(id,d):#O(n*m) m is considered to be the length of each id where O(m)is the time complexity of the comparison in the keys and n is the number of elements in the dictionary 
    for value in d.keys():
        if id.lower() == value.split(',')[0].lower():
            return True
    return False
# display fucntions for admin menu
def genders(d):#1 O(N) n is the number of elements in the dictionary depends on whats the user enters 
    males=0
    females=0
    for value in d.values():
      if value.split(',')[2].lower()=='male': # after splitingat , the genders index will be at 2
          males+=1
      elif value.split(',')[2].lower()=='female':
          females+=1
    
    return f'the number of females are {females} and the number of males {males}'
#https://www.tutorialspoint.com/How-to-get-formatted-date-and-time-in-Python#:~:text=To%20convert%20a%20datetime%20object,hh%3Amm%3Ass%20format.
import datetime
def add_emp():#2 O(k+l) since there are 2 for loops next to each other
    username = input('Enter username: ')
    while True:
        gender = input('Enter gender (male/female): ')
        if gender.lower() =='male' or gender.lower()=='female':
            break
        else:
            print("Invalid gender. Please enter 'male' or 'female'.")
    while True:
        salary_input =input('Enter salary:')
        if salary_input.isdigit():
            salary = int(salary_input)
            break
        else:
            print("Invalid salary. Please enter a valid number.")
    dx = datetime.datetime.now().strftime('%Y%m%d') # the link source is next to the function from where i got it 

    with open('Data.txt', 'r') as lines:
        count = len(lines.readlines()) + 1 # i counted the lines and since its a new employee so its an extra line 
    employee_id = f'emp00{count}'
    new_line = f'{employee_id},{username},{dx},{gender},{salary}'
    with open('Data.txt', 'a') as file:
        file.write('\n'+new_line) # writing to the text file on a new line the new employee data
    print("New employee has been added")

def display_data():#3 O(1) DISPLAYING 1 output 
    with open('Data.txt','rt') as file:
        lines=  file.readlines()
        for line in lines:
            print(line.strip('\n'))# removes the \n  spaces between the text files lines that are being printed  

def update_salary(d):#4 O(N) diplayed according to the users input 
    while True:
        emp_id = input('Enter employee id: ')
        if find_id(emp_id, d):
            salary = float(input('Enter new slary: '))
            with open('Data.txt', 'r') as file:
                lines = file.readlines()
            with open('Data.txt', 'w') as file:
                for line in lines:
                    if emp_id in line:
                        data = line.split(',') # split lines on each , 
                        new_salary = int(salary) 
                        str_salary = str(new_salary) 
                        data[4] = str_salary# when the data was splited its shjoe that the salary is on index 4 so we add the new salary on index 4
                        new_line = ','.join(data) # added the new data to the line 
                        file.write(new_line + '\n')
                        print(f'Salary has been updated  to {data[4]}')
                    else:
                        file.write(line)
            break
        else:
            print('Employee not found!')

def del_emp():#5# O(N) also depends on the users input #https://www.csnewbs.com/python-10c-remove-edit-lines#:~:text=Deleting%20Lines%20in%20a%20File&text=open%20the%20file%20in%20read,to%20input%20the%20exact%20line&text=Then%20open%20the%20file%20in,file%20isn't%20equal%20to&text=The%20line.
  emp_id=input('enter employee id: ')
  found=False
  with open('Data.txt','r') as file:
      lines=file.readlines()
  with open('Data.txt','w') as file:
      for line in lines:
          if emp_id in line:  
              print('employee has been deleted')
          else:
              file.write(line)
  if not found:
      print('employee not found') # improvised the code a little bit according to whats asked for 

def raise_salary(d):
    while True:
        emp_id = input('Enter employee id: ')
        if find_id(emp_id, d):
            rase = float(input('Enter raise: ')) 
            with open('Data.txt', 'r') as file:
                lines = file.readlines()
            with open('Data.txt', 'w') as file:
                for line in lines:
                    if emp_id in line:
                        data = line.split(',') # splited data on each ,
                        new_salary = int(int(data[4]) * (rase/100)+int(data[4])) # since the slary in any line is on index 4 so we calculate it
                        str_salary = str(new_salary) # cast to string to re enter in the text file as string
                        data[4] = str_salary # the new raised salary is added to index 4
                        new_line = ','.join(data) # joinded to the new line
                        file.write(new_line + '\n') # write the new line 
                        print(f'Salary has been raised to {data[4]}')
                    else:
                        file.write(line)
            break
        else:
            print('Employee not found!')
def admin(d):#O(N) depends on the users input 
  while True:
      print('1.Display Statistics')
      print('2.Add an Employee')
      print('3.Display all Employees')
      print('4.Change Employees Salary')
      print('5.Remove Employee')
      print('6.Raise Employees Salary')
      print('7.Exit')
      x=input('enter a number:')
      
      if x=='1':
          print(genders(d))
      elif x=='2':
          add_emp()
      elif x=='3':
              display_data()
      elif x=='4':
            update_salary(d)
      elif x=='5':
            del_emp()
      elif x=='6':
          raise_salary(d)
      elif x=='7':
            exit()  
      else:
          print('incorrect input')  
      
# users menu
def get_salary(d, user):#O(n*m) which n represents the the items in the ictionary and m is the name of the salary
    for id,info in d.items(): 
        name = info.split(',')[0]# spliting items after each , which collects th names that  are located at index 0
        if name == user: 
            salary = info.split(',')[3]  # after finding if there is a user in the name  collect the slary in the data which is at index 3 
            print(f"Your salary is {salary}")
            return # exit loop when done 
def user(d, user_name):#O(N) depends ofn the users input
    while True:
        print('1. Check my Salary')
        print('2. Exit')
        x = input('Enter a number: ')
        
        if x == '1':
             get_salary(d, user_name)
        elif x == '2':
              exit()
        else:
            print("Incorrect input or number.")
i = 0
while i < 5: #O(1) constatnt loop repeating th same output
    user_input = input('Enter username: ')
    pws = input('Enter password: ')
    if user_input.lower() == 'admin' and pws.lower() == 'admin123123':
        print('WELCOME ADMIN')
        admin(d)
        break
    elif find_user(user_input, d) and pws == "":
        print('Hi user')
        user(d, user_input)
        break
    else:
        i += 1
        print('Wrong username or password')