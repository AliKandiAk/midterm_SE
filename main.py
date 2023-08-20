
d = {}
with open('Data.txt') as file:
    for line in file:
        parts = line.strip().split(",")
        key = parts[0]
        val = ",".join(parts[1:])  # Join the remaining parts to get the value
        d[key] = val

print(d)
def genders(d):#1
    males=0
    females=0
    for value in d.values():
      if value.split(',')[2].lower()=='male':
          males+=1
      elif value.split(',')[2].lower()=='female':
          females+=1
    
    return f'the number of females are {females} and the number of males {males}'

def find_user(user, d):
    for value in d.values():
        if user.lower() == value.split(',')[0].lower():
            return True
    return False


#https://www.tutorialspoint.com/How-to-get-formatted-date-and-time-in-Python#:~:text=To%20convert%20a%20datetime%20object,hh%3Amm%3Ass%20format.
import datetime

def add_emp():#2
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
    dx = datetime.datetime.now().strftime('%Y%m%d')

    with open('Data.txt', 'r') as lines:
        count = len(lines.readlines()) + 1
    employee_id = f'emp00{count}'
    new_line = f'{employee_id},{username},{dx},{gender},{salary}'
    with open('Data.txt', 'a') as file:
        file.write('\n' + new_line)
    print("New employee has been added")

def display_data():#3
    with open('Data.txt','rt') as file:
        lines=  file.readlines()
        for line in lines:
            print(line.strip('\n'))# removes the \n  spaces between the text files lines that are being printed  
def change_slary():#4
    while True:
        emloyee_name=input('enter employee id')
        if emloyee_name.lower():
            pass
def del_emp():#https://www.csnewbs.com/python-10c-remove-edit-lines#:~:text=Deleting%20Lines%20in%20a%20File&text=open%20the%20file%20in%20read,to%20input%20the%20exact%20line&text=Then%20open%20the%20file%20in,file%20isn't%20equal%20to&text=The%20line.
  emp_id=input('enter employee id: ')
  with open('Data.txt','r') as file:
      lines=file.readlines()
  with open('Data.txt','w') as file:
      for line in lines:
          if emp_id in line:
              print('employee has been delted')
          else:
              file.write(line)

def admin(d):
  while True:
      print('1.Display Statistics')
      print('2.Add an Employee')
      print('3.Display all Employees')
      print('4.Change Employees Salary')
      print('5.Remove Employee')
      print('6.Raise Employees Salary')
      print('7.Exit')
      x=input('enter a number:')
      if x.isdigit():
        if x==1:
          print(genders(d))
      
        elif x==2:
          add_emp()
        elif x==3:
              display_data()
        elif x==4:
            pass
        elif x==5:
            del_emp()
        elif x==7:
            exit()  
      else:
          print('incorrect input')  

def get_salary(d, user):
    for id, info in d.items():
        name = info.split(',')[0]
        if name == user:
            salary = info.split(',')[3]
            print(f"Your salary is {salary}")
            return  # Exit the loop once the salary is found
def user(d, user_name):
    while True:
        print('1. Check my Salary')
        print('2. Exit')
        x = input('Enter a number: ')
        if x.isdigit():
          if x == 1:
             get_salary(d, user_name)
          elif x == 2:
              exit()
        else:
            print("Incorrect input or number.")
i = 0
while i < 5:
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









# file=open('Data.txt','r')
# lines=file.readlines()
# file.close()
# ali='emp003'
# file=open('Data.txt','w')
# for line in lines:
#     if ali in line:
#       salary= ali.split(',')[4]*1.5
#     else:
#         file.write(line)
# file.close()

# ali = 'emp003'

# with open('Data.txt', 'r') as file:
#     lines = file.readlines()

# with open('Data.txt', 'w') as file:
#     for line in lines:
#         if ali in line:
#             parts = line.split(',')
#             new_salary = str(int(parts[4]) * 1.5)  # Multiply the salary by 1.5 and convert to string
#             parts[4] = new_salary
#             new_line = ','.join(parts)
#             file.write(new_line)
#         else:
#             file.write(line)

