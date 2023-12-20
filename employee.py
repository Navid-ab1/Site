import person
class Employee(person.Person):
    
    def __init__(self):
            super().__init__()
            self._work_experience = 0
            # self._degree_education = ''
            self.employee_lst = []


    @property
    def work_ex(self):
          return self._work_experience
    
    @work_ex.setter
    def work_ex(self,year):
          self._work_experience = self._work_experience + year


    def see_employee(self): 
        print(*self.employee_lst)
                
    def remove_employee(self,number):
        temp = []
        temp = self.employee_lst.copy()
        self.employee_lst.clear()
        for i in range(len(temp)):
            if temp[i][0] != number:
                self.employee_lst(temp[i])
            else:pass        
        temp.clear()
           
    def add_employee(self):
        self.name = input("Enter name: ")
        self.family = input("Enter familyname : ")
        self.phone = input("Enter phone number(phone should be started with zero and eleven length): ")
        self.provience = input("Enter provience(Tehran,Alborz): ")
        self.id = input("Enter id card: ")
        self.sex_prop = input('Enter your sex(Male,Female): ')
        self.degree_prop = input('Enter your last degree(Associates,Bachorlers,Masters,Doctorate): ')
        self.password = self.password_maker()
        self.employee_lst.append([self.id, self.name, self.family, self.phone, self.provience, self.password])
        
    