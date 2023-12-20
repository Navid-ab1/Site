from prints import *
import company
comp = company.Company()
def ceo_method(per,itm):
    print('-'*40)
    username = input("Enter your username")
    passw = input('Enter your enter password')
    if (comp.password_checker(passw) == True) and (comp.username_checker(username)== True):
        print(f"{c}\n{c_o}\n{c_t}\n{c_th}\n{c_f}\n{c_s}\n{c_se}\n{c_ei}" )
        ad_in = input()
        if ad_in == '1':
            per.add_admin()
        elif ad_in =='2':
            number = input(x_fi)
            per.remove_admins(number)
        elif ad_in =='3':
            per.see_admins()
        elif ad_in =='4':
            itm.add_item()
        elif ad_in =='5':
            itm.show_item()
        elif ad_in =='6': 
            id_re = int(input("Enter id's of item you want to remove: "))
            itm.remove_item(id_re)
        elif ad_in =='7':
            itm.show_categories()
        elif ad_in=='8': 
            id = int(input("Enter the id you want to modify: "))
            num = int(input("what is the number you want to put in there: "))
            itm.update_entity = (id,num)
