import person
class Admin(person.Person):
    x = False
    y = False
    def __init__(self):
        super().__init__()
        self.num_admin = 0 
        self.admin_lst =[]
        self.head_admins()
       

    def see_admins(self): 
        print(self.admin_lst)

    def head_admins(self):
        
        self.name = 'Ali'
        self.family = 'Karimi'
        self.phone = '09361035313'
        self.provience = 'Tehran'
        self.id = '38383838'
        self.password = '22443'
        self.sex_prop = 'Male'
        self.degree_prop = 'Masters'


   
        self.admin_lst.append([self.id,self.password, self.name, self.family, self.phone, self.provience,  
                               self.sex_prop , self.degree_prop
                            ])
       
    def remove_admins(self,number):
        temp = []
        temp = self.admin_lst.copy()
        self.admin_lst.clear()
        for i in range(len(temp)):
            if temp[i][0] != number:
                self.admin_lst.append(temp[i])
            else:pass        
        temp.clear()
           
    def add_admin(self):
        self.name = input("Enter name: ")
        self.family = input("Enter familyname : ")
        self.phone = input("Enter phone number(phone should be started with zero and eleven length): ")
        self.provience = input("Enter provience(Tehran,Alborz): ")
        self.id = input("Enter id card: ")
        self.sex_prop = input('Enter your sex(Male,Female): ')
        self.degree_prop = input('Enter your last degree(Associates,Bachorlers,Masters,Doctorate): ')
        self.password = self.password_maker()
        self.admin_lst.append([self.id,self.password, self.name, self.family, self.phone, self.provience,  
                               self.sex_prop , self.degree_prop
                            ])

    def entrant_checker(self,user_id,passw):
        for i in range(len(self.admin_lst)):
            if self.admin_lst[i][0] == user_id and self.admin_lst[i][1] == passw: Admin.y = True
            else: Admin.y = False
            return  Admin.y

        

    # def add_user():
    
    #def remove_user
    #def show_user

