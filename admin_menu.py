from prints import *
import admin,sys

ad = admin.Admin()
def admin_method(per,itm):
    temp = False
    print('-'*40)
    while True:
        print("")
        user_id = input("Enter your userid: ")
        passw = input("Enter you password: ")
        checker=ad.entrant_checker(user_id,passw)
        if checker == True:
            y = admin_functions(per,itm)
            return(y)
           
        else: 
            a =input("If you want to exit just print one or if you want to trying again just press Enter")
            if a == "1":  sys.exit()
            else:pass
def admin_functions(per,itm):
    
    print(f"{x_o} \n {x_t} \n {x_th} \n {x_f} \n {x_s} \n {x_se} \n {x_ei} \n {x_te}+\
        \n {x_elev} \n {x_twel}" )
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
    

    elif ad_in == '9':
        return(False)
    
    elif ad_in == '10': #add user
        pass