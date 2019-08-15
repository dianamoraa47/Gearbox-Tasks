class Money:
     def __init__(self, name, phone_number): 
          self.name = name
          self.phone_number = phone_number
          self.balance = 0    

     def deposit(self,amount):
          self.balance =  amount + self.balance
          message1 ="Hi {},confirmed you have deposited {} your balance is KSH {}.".format(self.name,amount,self.balance)
          print(message1) 
          
