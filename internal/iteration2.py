BDSC_MENU={4:{1:{"Juicies":1.001},2:{"Coconut Juicies":2.501},3:{"Moosies":2.001},4:{"Slushies":2.502}},
            3:{5:{"Potato Chips":2.503},6:{"Mrs Higgins Cookies":3.801}}, 
            2:{7:{"Hot noodles":3.802},8:{"Spaghetti Bun":1.501},9:{"Garlic Bread":2.002},10:{"Hot Dogs with Tomato sauce":4.001},11:{"Steam Buns(Chicken)":3.701},12:{"Peters Pie":4.90},13:{"Chicken Nugget Roll":4.801},14:{"Meatball Sub":4.802},15:{"Hash Brown":1.502}},
            1:{16:{"Water(small)": 2.504},17:{"Water(large)": 4.002},18:{"Lipton Ice Tea": 4.501},19:{"Aloe Ice Tea": 4.502},20:{"Hot Chocolate": 4.503}}}
with open("account.txt", "a") as f:# Create the txt file.
    f.write("")
order={}# This stores what the user ordered and quantity.
price={}# This stores the price of the order.
sum=0 #THis stores the total cost
calculation={}# This stores the food/drink names and price
calculation2={}# This stores the food/drink name number/order and price.
def math(): 
    global sum # Making sum global so it can be accessed to other functions
    while True:
        try:# using try and except incase user enters not a number.
            q=int(input("What would you like to order(type in (00) if you want to exit.)\n: "))
            if q in calculation2: # Using if statement 
                q2=int(input("Enter the quantity you want: ")) # Asking for the amount they want for the food/drink name.
                if q2>0:
                        multiple=calculation2[q]*q2 # This multiples the original food price name
                        sum=sum+multiple # Adding it to the total
                        for i in calculation: # Using for loop to check and store what the user ordered and the quantity. 
                            if calculation[i]==calculation2[q]:
                                order[i]=q2
                                price[calculation2[q]]=q2
                                break             
            elif q==00:
                menu()# This returns to the menu function. 
                return
            else:
                print("Please enter the numbers given.") 
        except ValueError:
            print("Enter a number")
def menu(): # This function displays the food menu
    global calculation,calculation2,sum
    while True:
        try:
            q=int(input("Would you like to order:\n Drinks(1)\n Lunch(2)\n Snacks(3)\n Frozen(4)\n Checkout(5)\n Cancel checkout(6)\n----------------------------------------------------------------------\n : "))
            if q in BDSC_MENU: # Checking before displaying the list by using if statement.
                category = BDSC_MENU[q]
                print("----------------------------------------------------------------------")
                for num in category:# Using many for loops to get to the price/name of the dictionary.
                    selection = category[num]
                    for name in selection:
                        print(f"{num}. {name}: ${selection[name]:.2f}") # This prints the number,food/drink name and price. 
                        calculation[name]=selection[name]# This stores the food/drink name and price
                        calculation2[num]=selection[name]# THis stores the food number and price.  
                        break
                print("----------------------------------------------------------------------")
                math() # This opens the math function. 
            elif q==5:
                    if sum==0:
                            print("Please order something") # Adding an if statement of zero if the user has not ordered yet. 
                    else:
                        print("You order is:\n--------------------------------------")
                        for i,pri in zip(order,price):# THis prints what the user ordered and the quantity of each food/drink. 
                            print(f"{i},${pri:.2f} x {order[i]}")
                        print("--------------------------------------")
                        print(f"The total price for your order is: ${sum:.2f}")# This prints the total. 
                        clear()
            elif q==6:
                clear()
                print("You order has been canceled.")
            else:
                print("Please enter the numbers given")
                break
        except ValueError:
            print("Please enter a number.")
def clear():
    order.clear()# Resetting the variables so it can be reused. 
    price.clear()
    sum=0
    login() 
def login():
    while True:   # Allows you to login to an existing schoool account or add your school account. 
            question=input("Welcome to the BDSC Cafe app!\n1. Add your school account:\n2. Login\n3. Remove password\n :")
            ac_account = input("Add your account name: ") 
            password = input("Enter your password: ")
            work=open("account.txt", "r")# Opening the txt file. 
            if question=="1":
                file=open('account.txt', 'a') # This allows the problem to write in the txt. 
                file.write(f'Account password for {ac_account} is: {password}\n') # Storig the account name and password. 
                print("Account has been added.")
            if question=="2":
                for i in work:#Using for loop to verify
                    f2=i.split() # Using split so the txt does not just randomly print. 
                    if ac_account in f2 and password in f2:
                        print("Login success")
                        menu()
                else:
                    print("Incorrect password or account name")
            if question=="3":
                for i in work:# Using for loop to check if username and password is in txt. 
                    if ac_account in i and password in i:
                        erase=open('account.txt','w')
                        erase.write('')
                    print("your account name and password has been erased")
                else:
                    print("There are no passwords saved for this account.")
            else:
                print("Please enter 1 out of the 3 numbers given.")  
def age():
    while True:# Adding age restrictions-13-18. 
        try:
            age = int(input("Please enter your age: "))
            if age >= 13 and age<=18: 
                print("You are eligible")
                login()
                break
            else:
                print("Your age must be between 13-18")
        except ValueError:
            print("Please enter a number")
age()

