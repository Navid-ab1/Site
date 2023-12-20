from prints import *
def employee_method(emp,itm):
    print('-'*40)
    print(f" " )
    ad_in = input(f"{e}\n{e_o}\n{e_t}\n{e_th}\n{e_f}\n{e_fi}\n{e_s}\n{e_se}\n{e_ei}")
    if ad_in == '1':
        emp.add_employee()
    elif ad_in =='2':
        number = input('Enter id that you want to remove: ')
        emp.remove_employee(number)
    elif ad_in =='3':
        emp.see_employee()
    elif ad_in =='4':
        itm.add_item()
    elif ad_in =='5':
        itm.show_item()
    elif ad_in =='6': 
        id_re = int(input("Enter id's of item you want to remove: "))
        itm.remove_item(id_re)
    elif ad_in =='7':
        itm.show_categories()
    elif ad_in=='8': #update entity
        id = int(input("Enter the id you want to modify: "))
        num = int(input("what is the number you want to put in there: "))
        itm.update_entity = (id,num)
