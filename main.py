
d = {}
with open('Data.txt') as file:
    for line in file:
        parts = line.strip().split(",")
        key = parts[0]
        val = ",".join(parts[1:])  # Join the remaining parts to get the value
        d[key] = val

print(d)

def find_user(user, d):
    for value in d.values():
        if user.lower() == value.split(',')[0].lower():
            return True
    return False
def genders(d):
    males=0
    females=0
    for value in d.values():
      if value.split(',')[2].lower()=='male':
          males+=1
      elif value.split(',')[2].lower()=='female':
          females+=1
    
    return f'the number of females are {females} and the number of males {males}'

#https://www.tutorialspoint.com/How-to-get-formatted-date-and-time-in-Python#:~:text=To%20convert%20a%20datetime%20object,hh%3Amm%3Ass%20format.
import datetime

def add_emp():
    username = input('Enter username: ')
    gender = input('Enter gender: ')
    salary = input('Enter salary: ')
    dx = datetime.datetime.now().strftime('%Y%m%d')
    
    with open('Data.txt', 'r') as lines:
        line_count = len(lines.readlines())+1
    employee_id = f'emp00{line_count}'
    new_line = f'{employee_id},{username},{dx},{gender},{salary}'
    with open('Data.txt', 'a') as file:
        file.write('\n'+new_line)
    print("New employee has been added")

add_emp()



def admin(d):
  while True:
      print('1.Display Statistics')
      print('2.Add an Employee')
      print('3.Display all Employees')
      print('4.Change Employees Salary')
      print('5.Remove Employee')
      print('6.Raise Employees Salary')
      print('7.Exit')
      x=int(input('enter a number:'))
      if x==1:
          genders(d)
      elif x==2:
          pass
      











# i=0
# while i <5:
#     user=input('enter username')
#     pws=input('entered password')
#     if user.lower()=='admin'and pws.lower()=='admin123123': 
#       print('WELCOME ADMIN')
#       break
#     elif find_user(user,d) ==True and pws=="":
#         print('hi user')
#         break
#     else:
#         i+=1
#         print('wrong user name or pass')
