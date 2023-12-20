import person
class Company(person.Person):
    x = False
    y = False
    def __init__(self):
        super().__init__()
        self._id = 993
        self._name = "Navid's company"
        self._name_ceo = 'Navid'
        self._address = 'No12,blvd,NY'
        self._password = '236393'


    def username_checker(self,user):
        
        if self._name_ceo == user:
            Company.y = True
        else:Company.y = False
        return Company.y


    def password_checker(self,passwd):
        if self._password == passwd:
            Company.x = True 
        else: Company.x = False
        return Company.x

