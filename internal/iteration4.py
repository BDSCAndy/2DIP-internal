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
    work=open("account.txt", "r")  # Opening the txt file. 
    def login():# This functions allows the user to login. 
            ac_account = entry_name.get()
            password = entryPass.get()# This is from the entry box below
            for i in work:
                f2=i.split() 
                if ac_account in f2 and password in f2:# Using for loop and if statement to confirm username and password. 
                    frame_2()
                    break
            else:
                messagebox.showerror('Incorrect password', 'Username or password is incorrect.')
    def reset(): # Erase list of passwords.
        found=False# This works better then the else statement. 
        ac_account = entry_name.get()
        password = entryPass.get() 
        for i in work:#Using for loop to verify before erasing password
            f2=i.split() # Using split so the txt does not just randomly print. 
            if ac_account in f2 and password in f2:#same if statement as login
                erase=open('account.txt','w')
                erase.write('')# Erases the data on txt file.
                found=True
                break
        if found:
            messagebox.showerror('Password','Password has been reset.')# Using message boxes
        if not found:
            messagebox.showerror('Incorrect password', 'Username or password is incorrect.')
  
    def add_acc():# This function allow you to add an account password
            ac_account = entry_name.get()
            password = entryPass.get()
            file=open('account.txt', 'a') # This allows the problem to write in the txt. 
            file.write(f'{ac_account} password: {password}\n')# This stores the entry input into the txt file. 
            messagebox.showinfo('Password', 'Username or password has been added.')
    # Placing the object in frame1
    welcome=Label(frame1,text=" WELCOME TO THE BDSC MENU APP!",font=("Arial",18))# Changing the font style and size.
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
    
    btn_add_account=Button(frame1,text="Add account",command=add_acc,width=11)# Activates the function when they press the button. 
    btn_add_account.grid(row=7,column=1,sticky=W)
    
    btn_reset=Button(frame1,text="Remove password",command=reset)
    btn_reset.grid(row=7,column=1)
    
    btnLogin=Button(frame1,text="Login",command=login,width=11)
    btnLogin.grid(row=7,column=1,sticky=E)
def frame_2(): # This frame shows the menu
    root.geometry('310x420')
    global frame2
    frame2=Frame(root)
    frame2.grid(row=0,column=0,sticky='nsew')
    root.title("Menu") 
    
    
    menu_lbl=Label(frame2,text="Select your order.",font=("Arial",20))
    menu_lbl.place(anchor=CENTER)
    menu_lbl.grid(row=0,column=2,padx=40)
    
    drink_button=Button(frame2,text="Drinks",width=10,height=2,font=("Arial",15),command=frame_3)
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
    
    checkout_button=Button(frame2,text="Checkout",width=10,height=2,font=("Arial",15),command=checkout_exit)
    checkout_button.place(anchor=CENTER)
    checkout_button.grid(row=5,column=2)
    
    
    logout_btn=Button(frame2,text="Logout",width=10,height=2,font=("Arial",15),command=log_out)
    logout_btn.place(anchor=CENTER)
    logout_btn.grid(row=6,column=2)
def checkout_exit():
    global pr_ice
    pr_ice=""
    if sum_1>0:
        for i in order:
            pr_ice=pr_ice+i
        messagebox.showinfo('Checkout',f"{pr_ice}\n----------------------------------\n Total price is: {sum_1:.2f}")
        messagebox.showinfo('Checkout',"Please collect your order at the school cafe.")
    else:
        messagebox.showerror('Checkout',"Please make an order.")
def log_out():
    global sum_1
    order.clear()
    sum_1=0
    frame0()
    
def frame_3():# List of drinks
    track_var=[]
    track_spinbox=[]
    root.geometry('250x300')
    global frame3
    frame3=Frame(root)
    frame3.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    
    category_names = list(BDSC_MENU[1].keys())
    category_price = list(BDSC_MENU[1].values())

    order_lbl=Label(frame3,text="Drinks:",font=("Arial",20))
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
                    spinbox.insert(0, 0)
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
                spinbox.insert(0, 0)
                found=True
        if found==True:
            messagebox.showinfo('Menu','Your order has been removed.') 
        else:
            messagebox.showerror('Menu','Please make an order')
        
        
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame3, from_=0, to=10,width=5)
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
def frame_4():# List of lunch
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
                    sum_1=sum_1+price*quantity # add the total price to sum_1]
                    var.set(0)
                    spinbox.delete(0, END)
                    spinbox.insert(0, 0)
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
                spinbox.insert(0, 0)
        if found==True:
            messagebox.showinfo('Menu','Your order has been removed.') 
        else:
            messagebox.showerror('Menu','Please make an order')
        
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame4, from_=0, to=10,width=5)
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
def frame_5():# List of snacks
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
                    spinbox.insert(0, 0)
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
                    spinbox.insert(0, 0)
            if found==True:
                messagebox.showinfo('Menu','Your order has been removed.') 
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame5, from_=0, to=10,width=5)
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
def frame_6():# list of frozen
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
                    spinbox.insert(0, 0)
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
                spinbox.insert(0, 0)
                found=True
        if found==True:
            messagebox.showinfo('Menu','Your order has been removed.') 
        else:
            messagebox.showerror('Menu','Please make an order')
        
        
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame6, from_=0, to=10,width=5)
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

