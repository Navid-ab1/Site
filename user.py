import person,item
it = item.Item()
class User(person.Person):
    order_status = ['Failed','Processing','Sent']
    def __init__(self):
        super().__init__()
        self._walletbalance = 0
        self._debtor = False
        self._historybuy = []

    @property
    def wallet(self):
        return self._walletbalance
    
    @wallet.setter
    def wallet(self,cash):
        try:
            if not (isinstance(cash,int) or isinstance(cash,float)):
                raise TypeError("Enter just number")
            else:self._walletbalance= cash
        except Exception as e:print(f"Error has been occoured. {e}  ")


    def buy_item(self,type_buy,item_name,item_num):
        if User.available_item(item_name,item_num):
            if ( type_buy == 'Cash') and  (self.wallet> item.Item.prop_price ) :
                self.wallet-=item.Item.prop_price
                self._debtor = False
                self._historybuy.append([self.id,self.name,item_name,item_num,self._debtor])
            elif type_buy == 'Installment':
                self._debtor = True
                self._historybuy.append([self.id,self.name,item_name,item_num,self._debtor])
            elif type_buy == 'paymentOnthespot':
                self._debtor = True
                self._historybuy.append([self.id,self.name,item_name,item_num,self._debtor])
            else:pass
        else:print("Enter correct number ")

    def available_item(self,item_name,item_num):
        if item_name in item.Item.categorys and it.compare_number(item_num):
            return True
        else:return False

    