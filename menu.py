import sys,admin,item,admin_menu,employee,employee_menu,admin_menu,user_menu
import ceo_menu
from prints import *
per = admin.Admin()
emp = employee.Employee()
itm = item.Item()
# user = user_menu()

while True:
    print('-'*40)
    print(f'{x_ni}\n{x}\nif you are Employee press 2: \n{y}')
    print('if you are CEO press 3: ')
    print('If you are User press 4: ')

    
    inp = input()
    if inp == '1':
        admin_menu.admin_method(per,itm)
    elif inp == '2':
        employee_menu.employee_method(emp,itm)
    elif inp =='3':
        ceo_menu.ceo_method(per,itm)
    elif inp =='4':
       user_menu.user_functions(itm)
    elif inp =='5':
        sys.exit()
