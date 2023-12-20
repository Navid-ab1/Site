class Item:
    categorys = ['Legumes','Vegetables','Detergents','Electronic']
    Legumes = ['Lentils','Peas','Chickpeas']
    def __init__(self,name = ''):
        self._name=name
        self._id = ''
        self._category = []
        self._available=False
        self._price = 0.0
        self._itemnum = 0
        # self._initnumber_entity=0
        # self._initremove_entity=0
        self._initadd_entity = 0
        self._show_items = []       #define for for print items

#-------------------------category----------------------

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self,cate):
        try:
            if not cate in Item.categorys:
                raise TypeError("Enter category correctly ")
            else:
                self._category = cate
                # self._available = True
        except Exception as e:print(f"Error {e} has been occoured ")



    @property
    def check_availablity(self):
        return self._available
    
    @check_availablity.setter
    def check_availablity(self):
        if self._itemnum >= 0:  self._available = True
        else : self._available = False


#-------------------------name----------------------
    def set_name(self,name_o):
        try : 
            if not name_o.isalpha(): raise TypeError('The name should be string.')
               
            elif len (name_o)>11: raise MemoryError('The name should be fewer than 11 character.')

            else: self._name = name_o

        except Exception as e:
            print(f"An error has occoured {e} ")
            
    def get_name(self):
        return self._name
    name = property(get_name,set_name)
   
#-------------------------id----------------------
    @property
    def prop_id(self):
        return self._id
    
    @prop_id.setter
    def prop_id(self,id):
        try:
            if not isinstance(id,int):
                raise TypeError("Enter just number")
            else:self._id = id
        except Exception as e:print(f"Error {e} has been occoured ")

#-------------------------price----------------------
    @property
    def prop_price(self):
        return self._price
    
    @prop_price.setter
    def prop_price(self,price):
        try:
            if not (isinstance(price,int) or isinstance(price,float)):
                raise TypeError("Enter just number")
            else:self._price = price
        except Exception as e:print(f"Error has been occoured. {e}  ")

#-------------------------number_entity(init,add,remove)----------------------

    @property
    def add_entity(self):
        return self._itemnum
    
    @add_entity.setter
    def add_entity(self,entity):
        try:
            if not (isinstance(entity,int) and entity>0):
                raise TypeError("Enter just number")
            else:self._itemnum +=  entity
            
        except Exception as e:print(f"Error has been occoured. {e}  ")
#                    -----remove entity------
    # @property
    # def remove_entity(self):
    #     return self._initnumber_entity
    
    # @remove_entity.setter
    # def remove_entity(self,entity):
    #     try:
    #         if not (isinstance(entity,int) and entity>0):
    #             raise TypeError("Enter just number")
    #         else:self._initnumber_entity = self._initnumber_entity-entity
    #     except Exception as e:print(f"Error has been occoured. {e}  ")

    @property
    def update_entity(self):
        return self._show_items
    @update_entity.setter
    def update_entity(self,id_num):
        id , num = id_num
        temp = list()
        temp = self._show_items.copy()
        self._show_items.clear()
        try:
            for i in range(len(temp)):
                if id == temp[i][0]:
                    temp[i][4] = num
                else : pass
        except Exception as e: print(f'{e} . not found')
        finally:
            self._show_items = temp.copy()
            temp.clear()
    
    def compare_number(self,num):
        if num <self._itemnum:
            return True
        else: return False

               
    def add_item(self):
        self.name = input("Enter name: ")
        self.prop_id = int(input("Enter item's id : "))
        self.category = input("Enter category: ")
        self.prop_price = eval(input("Enter price: "))
        self.add_entity = int(input("Enter item numbers that's can be add or remove"))
        # self.add_entity = int(input("Enter how many itmes do you buy: "))
        # self.remove_entity = int(input("Enter how many you sell items: "))
        self._show_items.append([self._id, self._name, self._category, self._price, self.add_entity])

    def remove_item(self,id):
        temp = list()
        temp = self._show_items.copy()
        self._show_items.clear()
        for i in range(len(temp)):
            if id!=temp[i][0]:
                self._show_items.append(temp[i][0])
            else:pass
        temp.clear()
        




    def show_item(self):                       #show item's that added to list 
        print(self._show_items)

    def show_categories(self):
        print(Item.categorys)




# add item barcode 
# day alarm for expired item 
        
#-------------test----------------------------
# obj = Item()
# obj.prop_price = "15"
# print(obj.prop_price)