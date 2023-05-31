from tkinter import* #(* means import all)
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.title("Login") 
sum_1 = 0
order=[]
with open("account.txt", "a") as f:# Creates the txt file
    f.write("")
BDSC_MENU={4:{"Juicies":1.001,"Coconut Juicies":2.501,"Moosies":2.001,"Slushies":2.502},
            3:{"Potato Chips":2.503,"Mrs Higgins Cookies":3.801}, #list of menu items
            2:{"Hot noodles":3.802,"Spaghetti Bun":1.501,"Garlic Bread":2.002,"Hot Dogs with Tomato sauce":4.001,"Steam Buns(Chicken)":3.701,"Peters Pie":4.90,"Chicken Nugget Roll":4.801,"Meatball Sub":4.802,"Hash Brown":1.502},
            1:{"Water(small)": 2.504,"Water(large)": 4.002,"Lipton Ice Tea": 4.501,"Aloe Ice Tea": 4.502,"Hot Chocolate": 4.503}}

def frame0():# Age
    root.geometry('210x100')# The frame size
    global frame_0# Making the frame global
    def age():# This functions makes sure the users age is between 13-18.
        try:
            age_num=int(age_entry.get())
            if age_num >=13 and age_num<=18: 
                frame_1()
            else:
                messagebox.showinfo('Age', 'You Age must be between 13-18')# Using message boxes. 
        except ValueError:
            messagebox.showinfo('age',"Please enter a number")

    frame_0=Frame(root)# Creating the frame
    frame_0.grid(row=0,column=0,sticky='nsew')   

    age_lbl=Label(frame_0,text="Please enter your age:")#Using labels,entry boxe and button
    age_lbl.grid(column=1,row=0)
    
    age_entry=Entry(frame_0,width=30)
    age_entry.grid(column=1,row=1,sticky=E,padx=10)# Placing the widget by using grid, padx for spacing between widgets. 

    age_button=Button(frame_0,text="Login",command=age)# Running the age function if they press the button
    age_button.grid(column=1,row=2)
def frame_1(): #Login 
    root.geometry('530x190')# New window size
    global frame1
    frame1=Frame(root)
    frame1.grid(row=0,column=0,sticky='nsew')
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
    # Placing the object in frame1
    welcome=Label(frame1,text=" WELCOME TO THE BDSC CAFE APP!",font=("Arial",18))# Changing the font style and size.
    welcome.place(anchor=CENTER)# Centering the text. 
    welcome.grid(row=0,column=1)
    by=Label(frame1,text="This program is made by Andy Li",font=("Arial",12))#using more entry, button labels for user login
    by.place(anchor=CENTER)
    by.grid(row=1,column=1)

    lb1=Label(frame1,text="Username:")
    lb1.grid(row=4,column=0)
    
    entry_name=Entry(frame1,width=76)
    entry_name.grid(row=4,column=1)
    
    lblPass=Label(frame1,text="Password:")
    lblPass.grid(row=5,column=0)
    
    entryPass=Entry(frame1,show="*",width=76)# Adding * when they enter the password 
    entryPass.grid(row=5,column=1)
    
    btn_add_account=Button(frame1,text="Add account",command=add_acc,width=20)# Activates the function when they press the button. 
    btn_add_account.grid(row=7,column=1,sticky=W)
    
    btn_reset=Button(frame1,text="Remove password",command=reset,width=20)
    btn_reset.grid(row=7,column=1)
    
    btnLogin=Button(frame1,text="Login",command=login,width=20)
    btnLogin.grid(row=7,column=1,sticky=E)

def frame_2(): # This frame shows the menu
    root.geometry('310x550')
    global frame2
    frame2=Frame(root)
    frame2.grid(row=0,column=0,sticky='nsew')
    root.title("Menu") 

    menu_lbl=Label(frame2,text="Select your order.",font=("Arial",20))
    menu_lbl.place(anchor=CENTER)# Adding in labels and buttons
    menu_lbl.grid(row=0,column=2,padx=40)
    
    drink_button=Button(frame2,text="Drinks",width=10,height=2,font=("Arial",15),command=frame_3)# adding functions when pressed.
    drink_button.place(anchor=CENTER)
    drink_button.grid(row=1,column=2)
    
    lunch_button=Button(frame2,text="Lunch",width=10,height=2,font=("Arial",15),command=frame_4)
    lunch_button.place(anchor=CENTER)
    lunch_button.grid(row=2,column=2)
    
    snacks_button=Button(frame2,text="Snacks",width=10,height=2,font=("Arial",15),command=frame_5)
    snacks_button.place(anchor=CENTER)
    snacks_button.grid(row=3,column=2)
    
    frozen_button=Button(frame2,text="Frozen",width=10,height=2,font=("Arial",15),command=frame_6)
    frozen_button.place(anchor=CENTER)
    frozen_button.grid(row=4,column=2)

    checkout_button2=Button(frame2,text="View order",width=10,height=2,font=("Arial",15),command=view_order)
    checkout_button2.place(anchor=CENTER)
    checkout_button2.grid(row=5,column=2)

    checkout_button=Button(frame2,text="Checkout",width=10,height=2,font=("Arial",15),command=checkout_exit)
    checkout_button.place(anchor=CENTER)
    checkout_button.grid(row=6,column=2)

    logout_btn2=Button(frame2,text="Cancel order",width=10,height=2,font=("Arial",15),command=cancel_order)
    logout_btn2.place(anchor=CENTER)
    logout_btn2.grid(row=7,column=2)
    
    logout_btn=Button(frame2,text="Logout",width=10,height=2,font=("Arial",15),command=log_out)
    logout_btn.place(anchor=CENTER)
    logout_btn.grid(row=8,column=2)
def checkout_exit():# This function shows the final order and price and clears it after words. 
    global pr_ice,sum_1
    pr_ice=""
    if sum_1>0:# Condition if the user has ordered something
        for i in order:
            pr_ice=pr_ice+i
        messagebox.showinfo('Checkout',f"{pr_ice}\n----------------------------------\n Total price is: {sum_1:.2f}")# Will display this in a message box
        messagebox.showinfo('Checkout',"Please collect your order at the school cafe your order has been reset.")# Telling user that it will reset the order
    else:# Condition incase user does not enter anything. 
        messagebox.showerror('Checkout',"Please make an order.")
        return
    order.clear()# Clears the list
    sum_1=0# Resets the total price to zero. 

def view_order():# This function lets the user view the price. 
    global pr_ice
    pr_ice=""
    if sum_1>0:# Same as above but does not reset it.
        for i in order:
            pr_ice=pr_ice+i
        messagebox.showinfo('Checkout',f"{pr_ice}\n----------------------------------\n Total price is: {sum_1:.2f}")
        return
    else:
        messagebox.showerror('Checkout',"Please make an order.")
def cancel_order():
    global sum_1
    order.clear()
    if sum_1>0:
        sum_1=0
        messagebox.showerror('Reset',"Your order has been reset.")
        return
    else:
        messagebox.showerror('Reset',"Please make an order")

def log_out():
    global sum_1
    order.clear()
    sum_1=0
    frame_1()
    messagebox.showerror('Reset',"Your order has been reset.")

def frame_3():# Shows the menu of drinks using checkboxes.
    track_var=[]# Keeps track of what the ticks from the checkbox. 
    track_spinbox=[]# Keeps track of the spin box
    root.geometry('250x300')
    global frame3#Making the frame global. 
    frame3=Frame(root)
    frame3.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    
    category_names = list(BDSC_MENU[1].keys())# Category names of drinks from dictionary
    category_price = list(BDSC_MENU[1].values())# Categiry names of the drink price. 

    order_lbl=Label(frame3,text="Drinks:",font=("Arial",20))
    order_lbl.grid(column=0,row=0,sticky=W)
    def ad_ord():# This function adds the price and quantity to the total price sum_1 and order list.        
        found=False# Using found to display a message box. 
        global sum_1,order
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            if var.get() ==1:# If its been ticked. 
                    quantity=int(spinbox.get())# Gets the the spinbox and converts it into a number. 
                    order.append(f"{name} - ${price:.2f}x{quantity}\n")# Stores the name price quanitty in a list. 
                    sum_1=sum_1+price*quantity # add the total price to sum_1]
                    var.set(0)# Unchecking it.
                    spinbox.delete(0, END) # Clearing and setting it back to zero
                    spinbox.insert(1, 1) 
                    found=True
        if found:
            messagebox.showinfo('Menu','Your order has been added.')
        else:# Incase they enter anything else. 
            messagebox.showerror('Menu','Please make an order')
        
    def remove_order():# This function removes the order. 
        found=False
        global sum_1,order  
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            quantity=int(spinbox.get())# Same ad order function. 
            if var.get() == 1 and quantity>=1:
                order.remove(f"{name} - ${price:.2f}x{quantity}\n")# But removes it form the list. 
                sum_1=sum_1-price*quantity # add the total price to sum_1
                var.set(0)
                spinbox.delete(0, END)
                spinbox.insert(1, 1)
                found=True
        if found==True:
            messagebox.showinfo('Menu','Your order has been removed.') 
        else:
            messagebox.showerror('Menu','Please make an order')
        
        
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame3, from_=1, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=E)

        chk_item = Checkbutton(frame3, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        
        track_spinbox.append(spinbox)
        
    add_order=Button(frame3,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=10,sticky=W)
    
    remove=Button(frame3,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=11,sticky=W)
    
    back=Button(frame3,text="Back",command=frame_2,width=23)
    back.grid(column=0,row=12,sticky=W)
def frame_4():# List of lunch same as frame3
    track_var=[]
    track_spinbox=[]
    root.geometry('350x400')
    global frame4
    frame4=Frame(root)
    frame4.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    
    category_names = list(BDSC_MENU[2].keys())
    category_price = list(BDSC_MENU[2].values())

    order_lbl=Label(frame4,text="Lunch:",font=("Arial",20))
    order_lbl.grid(column=0,row=0,sticky=W)
    def ad_ord():
        found=False
        global sum_1,order
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            if var.get() == 1:
                    quantity=int(spinbox.get())
                    order.append(f"{name} - ${price:.2f}x{quantity}\n")
                    sum_1=sum_1+price*quantity # add the total price to sum_1
                    var.set(0)
                    spinbox.delete(0, END)
                    spinbox.insert(1, 1)
                    found=True
        if found==True:
            messagebox.showinfo('Menu','Your order has been added.')
        else:
            messagebox.showerror('Menu','Please make an order')
        
    def remove_order():
        found=False
        global sum_1,order
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            if var.get() == 1:
                quantity=int(spinbox.get())
                order.remove(f"{name} - ${price:.2f}x{quantity}\n")
                sum_1=sum_1+price*quantity # add the total price to sum_1
                found=True
                var.set(0)
                spinbox.delete(0, END)
                spinbox.insert(1, 1)
        if found==True:
            messagebox.showinfo('Menu','Your order has been removed.') 
        else:
            messagebox.showerror('Menu','Please make an order')
        
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame4, from_=1, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=W)
        chk_item = Checkbutton(frame4, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        track_spinbox.append(spinbox)
        
    add_order=Button(frame4,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=10,sticky=W)
    
    remove=Button(frame4,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=11,sticky=W)
    
    back=Button(frame4,text="Back",command=frame_2,width=23)
    back.grid(column=0,row=12,sticky=W)
def frame_5():# List of snacks same as frame 3
    track_var=[]
    track_spinbox=[]
    root.geometry('350x250')
    global frame5
    frame5=Frame(root)
    frame5.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    
    category_names = list(BDSC_MENU[3].keys())
    category_price = list(BDSC_MENU[3].values())

    order_lbl=Label(frame5,text="Snacks:",font=("Arial",20))
    order_lbl.grid(column=0,row=0,sticky=W)
    def ad_ord():
        found=False
        global sum_1,order
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            if var.get() == 1:
                    quantity=int(spinbox.get())
                    order.append(f"{name} - ${price:.2f}x{quantity}\n")
                    sum_1=sum_1+price*quantity # add the total price to sum_1]
                    found=True
                    var.set(0)
                    spinbox.delete(0, END)
                    spinbox.insert(1, 1)
        if found==True:
            messagebox.showinfo('Menu','Your order has been added.')
        else:
            messagebox.showerror('Menu','Please make an order')
        
    def remove_order():
            found=False
            global sum_1,order
            for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
                if var.get() == 1:
                    quantity=int(spinbox.get())
                    order.remove(f"{name} - ${price:.2f}x{quantity}\n")
                    sum_1=sum_1+price*quantity # add the total price to sum_1
                    found=True
                    var.set(0)
                    spinbox.delete(0, END)
                    spinbox.insert(1, 1)
            if found==True:
                messagebox.showinfo('Menu','Your order has been removed.') 
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame5, from_=1, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=E)
        chk_item = Checkbutton(frame5, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        track_spinbox.append(spinbox)
        
    add_order=Button(frame5,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=10,sticky=W)
    
    remove=Button(frame5,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=11,sticky=W)
    
    back=Button(frame5,text="Back",command=frame_2,width=23)
    back.grid(column=0,row=12,sticky=W)
def frame_6():# list of frozen same as frame 3
    track_var=[]
    track_spinbox=[]
    root.geometry('250x300')
    global frame6
    frame6=Frame(root)
    frame6.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    
    category_names = list(BDSC_MENU[4].keys())
    category_price = list(BDSC_MENU[4].values())

    order_lbl=Label(frame6,text="Frozen:",font=("Arial",20))
    order_lbl.grid(column=0,row=0,sticky=W)
    def ad_ord():
        found=False
        global sum_1,order
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            if var.get() == 1:
                    quantity=int(spinbox.get())
                    order.append(f"{name} - ${price:.2f}x{quantity}\n")
                    sum_1=sum_1+price*quantity # add the total price to sum_1]
                    var.set(0)
                    spinbox.delete(0, END)
                    spinbox.insert(1, 1)
                    found=True
        if found==True:
            messagebox.showinfo('Menu','Your order has been added.')
        else:
            messagebox.showerror('Menu','Please make an order')
        
    def remove_order():
        found=False
        global sum_1,order
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            if var.get() == 1:
                quantity=int(spinbox.get())
                order.remove(f"{name} - ${price:.2f}x{quantity}\n")
                sum_1=sum_1+price*quantity # add the total price to sum_1
                var.set(0)
                spinbox.delete(0, END)
                spinbox.insert(1, 1)
                found=True
        if found==True:
            messagebox.showinfo('Menu','Your order has been removed.') 
        else:
            messagebox.showerror('Menu','Please make an order')
        
        
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame6, from_=1, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=E)
        chk_item = Checkbutton(frame6, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        track_spinbox.append(spinbox)
        
    add_order=Button(frame6,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=10,sticky=W)
    
    remove=Button(frame6,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=11,sticky=W)
    
    back=Button(frame6,text="Back",command=frame_2,width=23)
    back.grid(column=0,row=12,sticky=W)
frame0()
root.mainloop()

