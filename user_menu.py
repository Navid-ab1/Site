from prints import *
import admin,sys,user
us = user.User()


# def user_method(per,itm):
#     print('-'*40)
#     while True:
#         print("")
#         user_id = input("Enter your userid: ")
#         passw = input("Enter you password: ")
#         checker=ad.entrant_checker(user_id,passw)
#         if checker == True:
#             y = admin_functions(per,itm)
#             return(y)
           
#         else: 
#             a =input("If you want to exit just print one or if you want to trying again just press Enter")
#             if a == "1":  sys.exit()
#             else:pass
def user_functions(itm):
    print(f"{u}\n{u_o}\n{u_t}" )
    ad_in = input()
    if ad_in == '1':
        itm.show_categories()
    elif ad_in =='2':
       print(itm.show_categories())
       item_type = input()
       print(us.order_status)
       item_name=input()
       item_num =int( input("Enter numbers of you want to buy: ")
)
       us.buy_item(item_type,item_name,item_num)

    # elif ad_in =='3':
    #     per.see_admins()
    # elif ad_in =='4':
    #     itm.add_item()
    # elif ad_in =='5':
    #     itm.show_item()
    # elif ad_in =='6': 
    #     id_re = int(input("Enter id's of item you want to remove: "))
    #     itm.remove_item(id_re)
    # elif ad_in =='7':
    #     itm.show_categories()
    # elif ad_in=='8': 
    #     id = int(input("Enter the id you want to modify: "))
    #     num = int(input("what is the number you want to put in there: "))
    #     itm.update_entity = (id,num)
    

    # elif ad_in == '9':
    #     return(False)
    
    # elif ad_in == '10': #add user
    #     pass