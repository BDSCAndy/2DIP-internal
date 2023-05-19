from tkinter import* #(* means import all)
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title("Login") 
sum_1 = 0
order=[]
with open("account.txt", "a") as f:
    f.write("")
BDSC_MENU={4:{"Juicies":1.001,"Coconut Juicies":2.501,"Moosies":2.001,"Slushies":2.502},
            3:{"Potato Chips":2.503,"Mrs Higgins Cookies":3.801}, 
            2:{"Hot noodles":3.802,"Spaghetti Bun":1.501,"Garlic Bread":2.002,"Hot Dogs with Tomato sauce":4.001,"Steam Buns(Chicken)":3.701,"Peters Pie":4.90,"Chicken Nugget Roll":4.801,"Meatball Sub":4.802,"Hash Brown":1.502},
            1:{"Water(small)": 2.504,"Water(large)": 4.002,"Lipton Ice Tea": 4.501,"Aloe Ice Tea": 4.502,"Hot Chocolate": 4.503}}

def frame0():# age 
    root.geometry('210x195')
    global frame_0
    root.configure(bg="#5a183a")
    def age():
        try:
            age_num=int(age_entry.get())
            if age_num >=13 and age_num<=18: 
                frame_1()
            else:
                messagebox.showinfo('Age', 'You Age must be between 13-18')
        except ValueError:
            messagebox.showinfo('age',"Please enter a number")

    frame_0=Frame(root,bg="#5a183a")
    frame_0.grid(row=0,column=0,sticky='nsew') 
    
    image0 = Image.open("image0.png")
    resized_image3 = image0.resize((90, 90))
    photo0 = ImageTk.PhotoImage(resized_image3) 
    bdsc=Label(frame_0,image=photo0)
    bdsc.image=photo0
    bdsc.grid(row=0,column=1)

    age_lbl=Label(frame_0,text="Please enter your age:",background="#5a183a",foreground="White")
    age_lbl.place(anchor=CENTER)
    age_lbl.grid(column=1,row=1,sticky=S)
    
    age_entry=Entry(frame_0,width=30)
    age_entry.place(anchor=CENTER)
    age_entry.grid(column=1,row=2,sticky=E,padx=10,pady=10)

    age_button=Button(frame_0,text="Next",command=age)
    age_button.place(anchor=CENTER)
    age_button.grid(column=1,row=3)
def frame_1():# Login 
    root.geometry('540x390')
    global frame1
    frame1=Frame(root,bg="#5a183a")
    root.configure(bg="#5a183a")
    frame1.grid(row=0,column=0,sticky='nsew')#Noth south east and west(can appear anywhere in window)
    work=open("account.txt", "r")  # Opening the txt file. 
    def login():
            ac_account = entry_name.get()
            password = entryPass.get()
            for i in work:#Using for loop to verify
                f2=i.split() # Using split so the txt does not just randomly print. 
                if ac_account in f2 and password in f2:
                    frame_2()
                    break
            else:
                messagebox.showerror('Incorrect password', 'Username or password is incorrect.')
    def reset():
        found=False
        ac_account = entry_name.get()
        password = entryPass.get() 
        for i in work:#Using for loop to verify before erasing password
            f2=i.split() # Using split so the txt does not just randomly print. 
            if ac_account in f2 and password in f2:
                erase=open('account.txt','w')
                erase.write('')
                found=True
                break
        if found:
            messagebox.showerror('Password','Password has been reset.')
        if not found:
            messagebox.showerror('Incorrect password', 'Username or password is incorrect.')
  
    def add_acc():# This function allow you to add an account password
            ac_account = entry_name.get()
            password = entryPass.get()
            file=open('account.txt', 'a') # This allows the problem to write in the txt. 
            file.write(f'{ac_account} password: {password}\n')
            messagebox.showinfo('Password', 'Username or password has been added.')
    # Placing the object in frame1 

    welcome=Label(frame1,text=" WELCOME TO THE BDSC MENU APP!",font=("Arial",18,"bold"),background="#5a183a",fg="White")
    welcome.place(anchor=CENTER)
    welcome.grid(row=0,column=1)
    
    by=Label(frame1,text="This program is made by Andy Li",font=("Arial",12),background="#5a183a",fg="White")
    by.place(anchor=CENTER)
    by.grid(row=1,column=1)

    image1 = Image.open("padlock.png")
    resized_image = image1.resize((190, 150))
    photo = ImageTk.PhotoImage(resized_image)
    la_bel = Label(frame1, image=photo)
    la_bel.image = photo # Store a reference to the image to prevent garbage collection
    la_bel.grid(column=1,row=2)

    lb1=Label(frame1,text="Username:",background="#5a183a",fg="White")
    lb1.grid(row=4,column=0)
    
    entry_name=Entry(frame1,width=76)
    entry_name.grid(row=4,column=1,sticky=W,pady=3)
    
    lblPass=Label(frame1,text="Password:",background="#5a183a",fg="White")
    lblPass.grid(row=5,column=0)
    
    entryPass=Entry(frame1,show="*",width=76)
    entryPass.grid(row=5,column=1,sticky=W,pady=5)
    
    btn_add_account=Button(frame1,text="Add account",command=add_acc,width=20)
    btn_add_account.grid(row=7,column=1,sticky=W)
    
    btn_reset=Button(frame1,text="Remove password",command=reset,width=20)
    btn_reset.grid(row=7,column=1)
    
    btnLogin=Button(frame1,text="Login",command=login,width=20)
    btnLogin.grid(row=7,column=1,sticky=E)
def frame_2():# Menu
    root.geometry('430x540')
    global frame2
    frame2=Frame(root,bg="#5a183a")
    root.configure(background="#5a183a")
    frame2.grid(row=0,column=0,sticky='nsew')
    root.title("Menu") 

    menu_lbl=Label(frame2,text="     Select",font=("Arial ",20,"bold"),background="#5a183a",foreground="white")
    menu_lbl.place(anchor=CENTER)
    menu_lbl.grid(row=0,column=2,pady=10,sticky=E)

    menu_lbl2=Label(frame2,text="your order:",font=("Arial",20,"bold"),background="#5a183a",foreground="white")
    menu_lbl2.place(anchor=CENTER)
    menu_lbl2.grid(row=0,column=3,pady=10,sticky=W)

    image2 = Image.open("image6.jpg")# Drinks button
    resized_image2 = image2.resize((190, 150))
    photo2 = ImageTk.PhotoImage(resized_image2)    
    drink_button=Button(frame2,image=photo2,command=frame_3)
    drink_button.image=photo2
    drink_button.grid(row=1,column=2,pady=3,padx=3)
    
    image3 = Image.open("image7.jpg")#Lunch
    resized_image3 = image3.resize((190, 150))
    photo3 = ImageTk.PhotoImage(resized_image3) 
    lunch_button=Button(frame2,image=photo3,command=frame_4)
    lunch_button.image=photo3
    lunch_button.grid(row=1,column=3,pady=3,padx=3)
    
    image4 = Image.open("image8.jpg")#Snacks
    resized_image4 = image4.resize((190, 150))
    photo4 = ImageTk.PhotoImage(resized_image4) 
    snacks_button=Button(frame2,image=photo4,command=frame_5)
    snacks_button.image=photo4
    snacks_button.grid(row=2,column=2,pady=3,padx=3)
    
    image5 = Image.open("image9.jpg")#Frozen
    resized_image5 = image5.resize((190, 150))
    photo5 = ImageTk.PhotoImage(resized_image5)
    frozen_button=Button(frame2,image=photo5,command=frame_6)
    frozen_button.image=photo5
    frozen_button.grid(row=2,column=3,pady=3,padx=3)
    
    checkout_button=Button(frame2,text="View order",width=17,height=2,font=("Arial",15),command=view_orderr)
    checkout_button.grid(row=3,column=2,sticky=E,pady=3,padx=3)

    
    checkout_btn=Button(frame2,text="Checkout",width=17,height=2,font=("Arial",15),command=check_out)
    checkout_btn.grid(row=3,column=3)

    logout_btn=Button(frame2,text="Reset order",width=17,height=2,font=("Arial",15),command=reset_order)
    logout_btn.grid(row=4,column=2,pady=3,padx=3)

    logout_btn2=Button(frame2,text="Logout",width=17,height=2,font=("Arial",15),command=log_out)
    logout_btn2.grid(row=4,column=3,pady=3,padx=3)

def reset_order():# Functions for frame 2(menu)
    global sum_1
    if sum_1>0:
        order.clear()
        sum_1=0
        messagebox.showerror('Reset',"Your order has been reset.")
    else:
        messagebox.showerror('Checkout',"Please make an order.")
def log_out():
    global sum_1
    if sum_1>0:
        order.clear()
        sum_1=0
        messagebox.showerror('Reset',"Your order has been reset.")
    frame0()
def view_orderr():
    global pr_ice
    pr_ice=""
    if sum_1>0:
        for i in order:
            pr_ice=pr_ice+i
        messagebox.showinfo('Checkout',f"{pr_ice}\n----------------------------------\n Total price is: ${sum_1:.2f}")
    else:
        messagebox.showerror('Checkout',"Please make an order.")

def check_out():# Functions for frames 3-6
    global sum_1
    if sum_1>0:
        view_orderr()
        messagebox.showinfo('Checkout',"Please collect your order at the school cafe.")
        order.clear()
        sum_1=0
        frame0()
    else:
        messagebox.showerror('Checkout',"Please make an order.")
def ad_ord():
        found=False
        global sum_1,order
        for var, name, price, spinbox in zip(track_var, category_names, category_price, track_spinbox):
            if var.get() == 1 and spinbox != 0:
                    quantity=int(spinbox.get())
                    order.append(f"{name} - ${price:.2f}x{quantity}\n")
                    sum_1=sum_1+price*quantity # add the total price to sum_1]
                    var.set(0)
                    spinbox.delete(0, END)
                    spinbox.insert(0,0)
                    found=True
        if found==True:
            messagebox.showinfo('Menu','Your order has been added.')
            box4.delete(1.0,END)
            for i in order:
                box4.insert(END,i)
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
            box4.delete(1.0,END)
            for i in order:
                box4.insert(END,i)
            messagebox.showinfo('Menu','Your order has been removed.') 
        else:
            messagebox.showerror('Menu','Please make an order')
def frame_3():# Drinks
    global track_var,category_names,category_price,track_spinbox,box4,spinbox,spinbox,check
    track_var=[]
    track_spinbox=[]
    root.geometry('276x565')
    global frame3
    frame3=Frame(root)
    frame3.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    category_names = list(BDSC_MENU[1].keys())
    category_price = list(BDSC_MENU[1].values())
    order_lbl=Label(frame3,text="Drinks:",font=("Arial",20,"bold"))
    order_lbl.grid(column=0,row=0,sticky=W)
    
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame3, from_=0, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=E)
        chk_item = Checkbutton(frame3, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        track_spinbox.append(spinbox)
        
    add_order=Button(frame3,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=30,sticky=W)
    
    remove=Button(frame3,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=31,sticky=W)

    box4 = Text(frame3,width=20,height=10)
    box4.grid(column=0,row=32)
    
    back2=Button(frame3,text="Snacks",command=frame_5,width=10)
    back2.grid(column=0,row=33,sticky=W)

    back3=Button(frame3,text="Frozen",command=frame_6,width=10)
    back3.grid(column=0,row=34,sticky=W)

    back4=Button(frame3,text="Lunch",command=frame_4,width=10)
    back4.grid(column=0,row=35,sticky=W)

    logout_btn=Button(frame3,text="Checkout",width=23,command=check_out)
    logout_btn.grid(row=36,column=0,sticky=W)

    back=Button(frame3,text="Back to menu",command=frame_2,width=23)
    back.grid(column=0,row=37,sticky=W)
def frame_4():#Lunch
    global track_var,category_names,category_price,track_spinbox,box4,spinbox,spinbox,check

    track_var=[]
    track_spinbox=[]

    root.geometry('276x565')
    global frame4
    frame4=Frame(root)
    frame4.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    category_names = list(BDSC_MENU[2].keys())
    category_price = list(BDSC_MENU[2].values())

    order_lbl=Label(frame4,text="Lunch:",font=("Arial",20,"bold"))
    order_lbl.grid(column=0,row=0,sticky=W)
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame4, from_=1, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=W)
        chk_item = Checkbutton(frame4, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        track_spinbox.append(spinbox)
        
    add_order=Button(frame4,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=30,sticky=W)
    
    remove=Button(frame4,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=31,sticky=W)

    box4 = Text(frame4,width=20,height=5)
    box4.grid(column=0,row=32,sticky=W)
    
    back2=Button(frame4,text="Drinks",command=frame_3,width=10)
    back2.grid(column=0,row=33,sticky=W)

    back3=Button(frame4,text="Frozen",command=frame_6,width=10)
    back3.grid(column=0,row=34,sticky=W)

    back4=Button(frame4,text="Snacks",command=frame_5,width=10)
    back4.grid(column=0,row=35,sticky=W)

    logout_btn=Button(frame4,text="Checkout",width=23,command=check_out)
    logout_btn.grid(row=36,column=0,sticky=W)

    back=Button(frame4,text="Back to menu",command=frame_2,width=23)
    back.grid(column=0,row=37,sticky=W)
def frame_5():#Snacks
    global track_var,category_names,category_price,track_spinbox,box4,spinbox,spinbox,check
    track_var=[]
    track_spinbox=[]
    root.geometry('276x565')
    global frame5
    frame5=Frame(root)
    frame5.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    category_names = list(BDSC_MENU[3].keys())
    category_price = list(BDSC_MENU[3].values())

    order_lbl=Label(frame5,text="Snacks:",font=("Arial",20,"bold"))
    order_lbl.grid(column=0,row=0,sticky=W)        
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame5, from_=1, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=E)
        chk_item = Checkbutton(frame5, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        track_spinbox.append(spinbox)

    add_order=Button(frame5,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=20,sticky=W)
    
    remove=Button(frame5,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=21,sticky=W)

    box4 = Text(frame5,width=20,height=15)
    box4.grid(column=0,row=22)
    
    back2=Button(frame5,text="Drinks",command=frame_3,width=10)
    back2.grid(column=0,row=23,sticky=W)

    back3=Button(frame5,text="Frozen",command=frame_6,width=10)
    back3.grid(column=0,row=24,sticky=W)

    back4=Button(frame5,text="Lunch",command=frame_4,width=10)
    back4.grid(column=0,row=25,sticky=W)

    logout_btn=Button(frame5,text="Checkout",width=23,command=check_out)
    logout_btn.grid(row=26,column=0,sticky=W)

    back=Button(frame5,text="Back to menu",command=frame_2,width=23)
    back.grid(column=0,row=27,sticky=W)
def frame_6():#Frozen
    global track_var,category_names,category_price,track_spinbox,box4,spinbox,spinbox,check
    track_var=[]
    track_spinbox=[]
    root.geometry('276x565')
    global frame6
    frame6=Frame(root)
    frame6.grid(column=0,row=0,sticky='nsew')
    root.title("Menu")
    category_names = list(BDSC_MENU[4].keys())
    category_price = list(BDSC_MENU[4].values())

    order_lbl=Label(frame6,text="Frozen:",font=("Arial",20,"bold"))
    order_lbl.grid(column=0,row=0,sticky=W)
    for name,price in zip(category_names,category_price):
        check = IntVar()# Keeps track of whether the user has clicked on the check box or not 1(on) 0(off). 
        track_var.append(check)
        spinbox = Spinbox(frame6, from_=1, to=10,width=5)
        spinbox.grid(column=1,row=category_names.index(name)+1,sticky=E)
        chk_item = Checkbutton(frame6, text=f"{name}: ${price:.2f}", variable=check)
        chk_item.grid(column=0, row=category_names.index(name)+1, sticky=W)# Puts the next checkbox below the other. Through the use of index, which tells the program what to insert next. 
        track_spinbox.append(spinbox)
        
    add_order=Button(frame6,text="Add to order",command=ad_ord,width=23)
    add_order.grid(column=0,row=30,sticky=W)
    
    remove=Button(frame6,text="Remove from order.",command=remove_order,width=23)
    remove.grid(column=0,row=31,sticky=W)

    box4 = Text(frame6,width=20,height=13)
    box4.grid(column=0,row=32)
    
    back2=Button(frame6,text="Drinks",command=frame_3,width=10)
    back2.grid(column=0,row=33,sticky=W)

    back3=Button(frame6,text="Snacks",command=frame_5,width=10)
    back3.grid(column=0,row=34,sticky=W)

    back4=Button(frame6,text="Lunch",command=frame_4,width=10)
    back4.grid(column=0,row=35,sticky=W)

    logout_btn=Button(frame6,text="Checkout",width=23,command=check_out)
    logout_btn.grid(row=36,column=0,sticky=W)

    back=Button(frame6,text="Back to menu",command=frame_2,width=23)
    back.grid(column=0,row=37,sticky=W)
frame0()
root.mainloop()

