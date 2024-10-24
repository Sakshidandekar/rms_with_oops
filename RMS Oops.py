#!/usr/bin/env python
# coding: utf-8

# In[4]:


class RMS:     
    #RMS (Restaurant Management System)
    def __init__(self,restaurant_name,restaurant_menu):
        self.user_bill=0
        self.user_order=''
        self.user_pay=0
        self.menu=restaurant_menu
        self.rest_name=restaurant_name

    def welcome_user(self):
        #Welcome user
        print('Welcome to',self.rest_name)
    
    def display_menu(self):
    
        #Display Menu
         for i in self.menu:
            print(i.title(),self.menu[i])
    
    def take_order(self):#Take order
        self.user_order=input('Please place your order here:')
    
    def prepare_order(self):#preparing order
        import time
        print('Preparing your',self.user_order.title())
        time.sleep(1)
        self.user_bill=self.user_bill+self.menu[self.user_order.lower()]
    
    def serve_order(self):#Order serve
        print('Your order is ready!')
        print('Please enjoy your meal',self.user_order.title())
    
    def display_bill(self):#Display Bill
        print('Your Total Bill:',self.user_bill)
    
    def verify_payment(self):#Take Payment
        self.user_pay=int(input('Please pay your bill here:'))
        
        
        while self.user_pay<self.user_bill:
            print('Payment unsucessfully!')
            self.user_bill=self.user_bill-self.user_pay
            print('Please pay remaning',self.user_bill)
            self.user_pay=int(input('Please enter your bill here:'))
    
        if self.user_pay>self.user_bill:
            print('Payment Sucessful!')
            print('Here is your change:',self.user_pay-self.user_bill)
        else:
            pass
    
    def thank_user(self):#Thank user
        print('Thank you for visiting',self.rest_name)
    
    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.prepare_order()
            self.serve_order()
            self.user_rep=input('Do you want anything else?')
            while self.user_rep.lower()=='yes':
                self.repeat_order()
                self.user_rep=input('Do you want to order anything else?')
    
            self.display_bill()
            self.verify_payment()
            self.thank_user()
        else:
            print('Invalid Order!')
            self.order_process()
    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.prepare_order()
            self.serve_order()
        else:
            print('Invalid Order')
            self.repeat_order()

rn='Moonlight Cafe'
rm={'cold coffee':255,'latte':270,'snacks':250,'chai':150,'veg thali':300,'non veg thali':350,'chinese rice':230,'butter chicken':220}
moonlight_cafe=RMS(rn,rm)




# In[ ]:





# In[ ]:


#import library
import tkinter as tk

#create window
window=tk.Tk()

#change title of window
window.title('RMS OOPs')

#change window size
window.geometry('400x400')

tk.Label(window,text='Moonlight Cafe',font=('Helvetica',19)).place(x=115,y=50)
tk.Button(window,text='Start',width=15,command=moonlight_cafe.order_process).place(x=140,y=190)

#ye agar nhi likhoge toh window nai dikhegi
window.mainloop()


# In[ ]:





# In[ ]:




