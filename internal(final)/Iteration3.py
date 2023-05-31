from tkinter import* #(* means import all)
from tkinter import messagebox
from tkinter import ttk    #Imports from tkinter needed. 
root=Tk()
root.title("Login") 
with open("account.txt", "a") as f:
    f.write("")
sum_1 = 0# Keeps track of total price
order=[]# Stores what the user ordered and quantity.
BDSC_MENU={4:{"Juicies":1.001,"Coconut Juicies":2.501,"Moosies":2.001,"Slushies":2.502},#dictionary of drinks and food.
            3:{"Potato Chips":2.503,"Mrs Higgins Cookies":3.801}, 
            2:{"Hot noodles":3.802,"Spaghetti Bun":1.501,"Garlic Bread":2.002,"Hot Dogs with Tomato sauce":4.001,"Steam Buns(Chicken)":3.701,"Peters Pie":4.90,"Chicken Nugget Roll":4.801,"Meatball Sub":4.802,"Hash Brown":1.502},
            1:{"Water(small)": 2.504,"Water(large)": 4.002,"Lipton Ice Tea": 4.501,"Aloe Ice Tea": 4.502,"Hot Chocolate": 4.503}}

def frame0():# THis function asks for users age. 
    root.geometry('210x100')# First frame asks for user age.
    global frame_0
    def age():# Adding conditions.
        try:
            age_num=int(age_entry.get())
            if age_num >=13 and age_num<=18: 
                frame_1()# Goes to the next frame
            else:
                messagebox.showerror('Age', 'You Age must be between 13-18')
        except ValueError:
            messagebox.showerror('age',"Please enter a number")

    frame_0=Frame(root)
    frame_0.grid(row=0,column=0,sticky='nsew')# Displaying entry,label and button. 

    age_lbl=Label(frame_0,text="Please enter your age:")
    age_lbl.grid(column=1,row=0)
    
    age_entry=Entry(frame_0,width=30)
    age_entry.grid(column=1,row=1,sticky=E,padx=10)

    age_button=Button(frame_0,text="Login",command=age)
    age_button.grid(column=1,row=2)
def frame_1():# This function displays a login menu
    root.geometry('270x150')
    global frame1# Making it into a frame so i can use grid. 
    frame1=Frame(root)
    frame1.grid(row=0,column=0,sticky='nsew')#Noth south east and west(can appear anywhere in window)
    def add_acc():# This function allow you to add an account password
            ac_account = entry_name.get()
            password = entryPass.get()
            if not ac_account or not password:
                messagebox.showerror('Incorrect password', 'Please make an entry')
                return# Ends the function
            file=open('account.txt', 'a') # This allows the problem to write in the txt. 
            file.write(f"{ac_account}:{password}\n")
            messagebox.showinfo('Password', 'Username or password has been added.')
    def login():# This function allows the user to log in.
        ac_account = entry_name.get() # Retrieiving name and password from the entry.
        password = entryPass.get()
        if not ac_account or not password:# If the user has not entered anything it will display a message box
            messagebox.showerror('Missing Information', 'Please make an entry')
            return
        with open('account.txt', 'r') as file:# Opening txt file. 
            login_now = file.readlines()# Making the it reads everything in the txt file to avoid error. 
        for i in login_now:# Using for loop to check if user input is in the txt file. 
            account_login, ac_password = i.strip().split(":")# This gets rid of the ":" and sets the username and password into the variables.
            if ac_account == account_login and ac_password == password:# Runnning condition before the user is logged in. 
                frame_2()
                return
        else:# Condition if the user enters the wrong password. 
            messagebox.showerror('Incorrect Password', 'Username or password is incorrect.')

    def reset():# This function erases whats on the txt file. 
        found=False
        ac_account = entry_name.get()
        password = entryPass.get()
        if not ac_account or not password:
            messagebox.showerror('Incorrect password', 'Please make an entry')
            return
        with open('account.txt', 'r') as file:# same as login function 
            login_now = file.readlines()
        for i in login_now:
            account_login, ac_password = i.strip().split(":")
            if ac_account == account_login and ac_password == password:
                    erase=open('account.txt','w')# But it erases the txt file. 
                    erase.write('')
                    found=True# Using found so the user will know there password has been cleared. 
        if found:
            messagebox.showerror('Password','Password has been reset.')
            return
        if not found:# This is the same as else but if not found is more apropirate. 
            messagebox.showerror('Incorrect password', 'Username or password is incorrect.')
            return
    welcome=Label(frame1,text="WELCOME TO THE BDSC CAFE APP")
    welcome.grid(row=0,column=1,)

    lb1=Label(frame1,text="Username:")# Using labels,buttons
    lb1.grid(row=1,column=0)
    
    entry_name=Entry(frame1,width=30)
    entry_name.grid(row=1,column=1)
    
    lblPass=Label(frame1,text="Password:")
    lblPass.grid(row=2,column=0)
    
    entryPass=Entry(frame1,show="*",width=30)
    entryPass.grid(row=2,column=1)
    
    btnLogin=Button(frame1,text="Login",command=login,width=10)
    btnLogin.grid(row=3,column=1,sticky=W)

    btn_add_account=Button(frame1,text="Add account",command=add_acc,width=12)
    btn_add_account.grid(row=3,column=1,sticky=E)
    
    btn_reset=Button(frame1,text="Remove password",command=reset)
    btn_reset.grid(row=4,column=1)
def frame_2():# Shows the menu.
    root.geometry('230x200')
    global frame2
    frame2=Frame(root)
    frame2.grid(row=0,column=0,sticky='nsew')
    root.title("Menu")
    
    category_names = list(BDSC_MENU[4].keys())# Assigning specific parts of the dictionary being drinks names
    category_price = list(BDSC_MENU[4].values())# prices

    category_names2 = list(BDSC_MENU[3].keys())# Lunch names
    category_price2 = list(BDSC_MENU[3].values())#Prices of lunch

    category_names3 = list(BDSC_MENU[2].keys())# Snacks
    category_price3 = list(BDSC_MENU[2].values())#Prices of snacks

    category_names4 = list(BDSC_MENU[1].keys())# Frozen
    category_price4 = list(BDSC_MENU[1].values())

    order_label=Label(frame2,text="What would you like to order?")# Widgets for the menu. 
    order_label.grid(row=1,column=0)
    combo = ttk.Combobox(frame2, values=[f"{name} - ${price:.2f}" for name, price in zip(category_names, category_price)])# Using ofr loop to print 
    combo.set("Frozen")
    combo.grid(row=2,column=0)
    spinbox1 = Spinbox(frame2, from_=0, to=10,width=5)# Using spin box to select quantity.
    spinbox1.grid(row=2,column=1)

    combo2 = ttk.Combobox(frame2, values=[f"{name} - ${price:.2f}" for name, price in zip(category_names2, category_price2)])
    combo2.set("Snacks")
    combo2.grid(row=3,column=0)
    spinbox2 = Spinbox(frame2, from_=0, to=10,width=5)
    spinbox2.grid(row=3,column=1)
    
    combo3 = ttk.Combobox(frame2, values=[f"{name} - ${price:.2f}" for name, price in zip(category_names3, category_price3)])
    combo3.set("Lunch")
    combo3.grid(row=4,column=0)
    spinbox3 = Spinbox(frame2, from_=0, to=10,width=5)
    spinbox3.grid(row=4,column=1)

    combo4 = ttk.Combobox(frame2, values=[f"{name} - ${price:.2f}" for name, price in zip(category_names4, category_price4)])
    combo4.set("Drinks")
    combo4.grid(row=5,column=0)
    spinbox4 = Spinbox(frame2, from_=0, to=10,width=5)
    spinbox4.grid(row=5,column=1)
 
    def math(): # Calculates the total cost and stores the order name price and quantyity into the order list. 
        quantity1 = int(spinbox1.get())
        quantity2 = int(spinbox2.get())# Assigning variables to make the conditions easier to work with. 
        quantity3 = int(spinbox3.get())# Variables of quantity from spinbox
        quantity4 = int(spinbox4.get())
        p1 = category_price[combo.current()] 
        p2 = category_price2[combo2.current()]
        p3 = category_price3[combo3.current()]# Variables of names from dictionary that are selected from the combobox
        p4 = category_price4[combo4.current()]
        n1=category_names[combo.current()]
        n2=category_names2[combo2.current()]
        n3=category_names3[combo3.current()]# Prices that are from the dictionary and are selected from the combo box. 
        n4=category_names4[combo4.current()]
        global sum_1,order # Making variables global so it can be accessed outside of other functions.
        found=False
        if quantity1 >0:
            order.append(f"\n{n1}: ${p1:.2f} X{quantity1}")# Condititons before it can store the name, price and quantity in the list.
            found=True
        if quantity2 >0:
            order.append(f"\n{n2}: ${p2:.2f} X{quantity2}")
            found=True
        if quantity3 >0:
            order.append(f"\n{n3}: ${p3:.2f} X{quantity3}")
            found=True
        if quantity4 >0:
            order.append(f"\n{n4}: ${p4:.2f} X{quantity4}")
            found=True
        if found:
            messagebox.showinfo('Menu','Your order has been added.')# Tell the user it works
            subtotal = quantity1 * p1 + quantity2 * p2 + quantity3 * p3 + quantity4 * p4# Adds it to the total cost. 
            sum_1=sum_1+subtotal
        if not found:
            messagebox.showinfo('Menu','Please make the order.')
    def view_order():
        global pr_ice
        pr_ice=""
        for nam in order:# THis prints what the user ordered and the quantity of each food/drink. 
            pr_ice=pr_ice+f"{nam}\n----------------------------------"# Displaying it in a message box. 
        pr_ice=pr_ice+f"\nTotal price: ${sum_1:.2f}"
        messagebox.showinfo('Menu',pr_ice)
    def remove_item():
        global sum_1# Same as math function but subtracts and removes from the list. 
        quantity1 = int(spinbox1.get())
        quantity2 = int(spinbox2.get())# Assigning variables to make the conditions easier to work with. 
        quantity3 = int(spinbox3.get())# Variables of quantity from spinbox
        quantity4 = int(spinbox4.get())
                    
        p1 = category_price[combo.current()] 
        p2 = category_price2[combo2.current()]
        p3 = category_price3[combo3.current()]# Variables of names from dictionary that are selected from the combobox
        p4 = category_price4[combo4.current()]
 
        n1=category_names[combo.current()]
        n2=category_names2[combo2.current()]
        n3=category_names3[combo3.current()]# Prices that are from the dictionary and are selected from the combo box. 
        n4=category_names4[combo4.current()]
        if quantity1 >0:
            order.remove(f"\n{n1}: ${p1:.2f} X{quantity1}")
        if quantity2 >0:
            order.remove(f"\n{n2}: ${p2:.2f} X{quantity2}")
        if quantity3 >0:
            order.remove(f"\n{n3}: ${p3:.2f} X{quantity3}")# Removes from list. 
        if quantity4 >0:
            order.remove(f"\n{n4}: ${p4:.2f} X{quantity4}")
        if quantity1 >0 or quantity2 >0 or quantity3 >0 or quantity4 >0:
            messagebox.showinfo('Order',"Your order has been removed")
        subtotal = quantity1 * p1 + quantity2 * p2 + quantity3 * p3 + quantity4 * p4
        sum_1=sum_1-subtotal# Subtracts what the user selected from the total price. 
    def checkout():
        global sum_1 # THis resets the program. 
        view_order()
        cancel_order()
        messagebox.showinfo('Checkout',"Please collect your order at the school cafe.")
        frame0()
    def cancel_order():
        global sum_1
        sum_1 = 0
        order.clear()
        messagebox.showinfo('Checkout',"Your order has been cleared")

    btn_add_order = Button(frame2, text="Add to order",command=math,width=10)# Buttons to display in the menu function.
    btn_add_order.grid(row=6,column=0,sticky=W)
    
    btn_check = Button(frame2, text="View order",command=view_order,width=10)
    btn_check.grid(row=6,column=0,sticky=E)
    
    btn_remove = Button(frame2, text="Checkout",command=checkout,width=10) 
    btn_remove.grid(row=8,column=0,sticky=W)
    
    btn_checkout = Button(frame2, text="Remove order",command=remove_item,width=10) 
    btn_checkout.grid(row=8,column=0,sticky=E) 

    btn_checkout2 = Button(frame2, text="Cancel entire order",command=cancel_order,width=22) 
    btn_checkout2.grid(row=9,column=0,sticky=W) 
frame0()# THis is what starts the program initially. 
root.mainloop()

