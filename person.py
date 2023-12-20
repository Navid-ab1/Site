import random
import datetime
class Person:
    provience_lst= ['Tehran','tehran','Alborz','alborz']
    degree_lst =['Associates','Bachorlers','Masters','Doctorate']
    sex = ['Male','Female']
    def __init__(self):
        self._name = ''
        self._family_name = ''
        self._provience = ''
        self._phoneNumber = ''
        self._id = 'user'
        self._degree = ''
        self._sex = ''
        self._password = ''

#------------------degree------------------- 

    @property
    def degree_prop(self):
        return self._degree
    
    @degree_prop.setter
    def degree_prop(self,degree):
        try:
            if degree in Person.degree_lst:
                self._degree = degree
            else:
                raise TypeError("Enter degree properly : ")
        except Exception as e:
            print(e)  

#------------------sex------------------- 

    @property
    def sex_prop(self):
        return self._degree

    @sex_prop.setter
    def sex_prop(self,sex_g):
        try:
            if sex_g in Person.sex:
                self._sex = sex_g
            else:
                raise TypeError("Enter gender properly: ")
        except Exception as e:
            print(e) 

#------------------name-------------------  
    def set_name(self,name):
        try:self._name = name
        except Exception as e:print(e)
    
    def get_name(self):
        return self._name
    
#------------------family_name------------- 
    def set_family(self,family_name):
        try: self._family_name = family_name
        except Exception as e:print(e)
    
    def get_family(self):
        return self._family_name
    
#------------------provience---------------  
    def set_provience(self,provience):
        if provience in Person.provience_lst:
            self._provience = provience
        else:self._provience = ''

    def get_provience(self):
        return self._provience
#------------------phone_number------------
    def set_phoneNumber(self,phoneNumber):
        try:
            if len(phoneNumber) == 11 and phoneNumber[0] == '0':
                self._phoneNumber = phoneNumber
            else : raise KeyError('Enter corrected format: ')
        
        except Exception as e:print(e)

    def get_phoneNumber(self):
        return self._phoneNumber
#------------------id_card-----------------  
    def set_id(self,id):
        try:self._id = id
        except Exception as e:print(e)

    def get_id(self):return self._id
#------------------password----------------
    def set_password(self,passw):
        try:self._password = passw
        except ValueError as e: print(e)
    
    def get_password(self):return self._password
    
#__________________decorator_________________
    name = property(get_name,set_name)
    family = property(get_family,set_family)
    phone = property(get_phoneNumber,set_phoneNumber)
    provience = property(get_provience,set_provience)
    id = property(get_id,set_id)
    password =property(get_password,set_password)
    

#------------------Password_maker-------------
    def password_maker(self):
        x = ''
        passwod = ''
        res = list()
        x2 = x = self.name+self.family+self.phone + str(datetime.datetime.now())
        x = self._name[::2] +self._family_name[::3] +self._phoneNumber + str(datetime.datetime.now())
        passwod = '12345'
        # for i in x :
        #     res.append(i)

        # for i in range(8):
        #     passwod+=random.choice(res)
        return passwod    
#----------------------------------------------
    def __repr__(self):
        return(f'This is refer show {self.id} , {self.name}+\
               ,{self.family},{self.password}')



