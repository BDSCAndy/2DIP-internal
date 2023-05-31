FROZEN={"Juicies":1.00,"Coconut Juicies":2.50,"Moosies":2.00,"Slushies":2.50} # Creating dictionery for all food menu, frozen,snakcs,lunch drinks. 
SNACKS={"Potato Chips":2.50,"Mrs Higgins Cookies":3.80}
LUNCH={"Hot noodles":3.80,"Spaghetti Bun":1.50,"Garlic Bread":2.00,"Hot Dogs with Tomato sauce":4.00,"Steam Buns(Chicken)":3.70,"Peters Pie":4.90,"Chicken Nugget Roll":4.80,"Meatball Sub":4.80,"Hash Brown":1.50}
DRINKS = {"Water(small)": 2.50, "Water(large)": 4.00, "Lipton Ice Tea": 4.50, "Aloe Ice Tea": 4.50, "Hot Chocolate": 4.50}
ACC_PASS={}
order={}
sum=0
def menu(): # Function that gives the choices of what the user wants to order.  
    while True: # Using while loop. 
        question=input("Would you like to order:\n Drinks(a)\n Lunch(b)\n Snacks(c)\n Frozen(d)\n Checkout(e)\n: ")
        if question=="a":
            for i in DRINKS: # Using for loop to print the dictionaries. 
                print(i, f"${DRINKS[i]:.2f}") # This is the printing format
            math() # This opens the math function.
        elif question=="b":
            for i2 in LUNCH:
                print(f"{i2}: ${LUNCH[i2]:.2f}")# This is repeated for all dictioaries.
            math()
        elif question=="c":
            for i3 in SNACKS:
                print(f"{i3}: ${SNACKS[i3]:.2f}")
            math()
        elif question=="d":
            for i4 in FROZEN:
                print(f"{i4}: ${FROZEN[i4]:.2f}")
            math()
        elif question=="e": # This tells the user the total price based off what they ordered.
            global sum
            if sum==0:
                print("Please make an order")
            else:
                print(f"Your order is: {order}\nThe total price is ${sum:.2f}\nPlease collect your order at the cafe.")
                sum=0
                order.clear()
                login()
                break
        else:# Incase the user enters anything other a,b,c,d,e It will loop back to the first input.
             print("Enter the numbers given")
def math(): # This funtion will add what the user ordered to the total price.
    global sum,order #This ensures the sum can be printed in another function.
    while True:# Using while loop to ask the question. 
        q=input("What would you like to order(ENTER NAME ONE TO ONE)\n: ") # This asks the user what they want to order. 
        if q in DRINKS:# I added conditions before adding the adding it to the total incase its not on the menu. 
            sum=sum+DRINKS[q] #This adds what the user ordered into the total price.
            order[q]=DRINKS[q]
        elif q in LUNCH:# Conditions/adding to toal are repeated.
            sum=sum+LUNCH[q]
            order[q]=LUNCH[q]
        elif q in SNACKS:
            sum=sum+SNACKS[q]
            order[q]=LUNCH
        elif q in FROZEN:
            sum=sum+FROZEN[q]
            order[q]=FROZEN[q]
        else:# If its not in the dictionary then it go back to the first question. 
            print("There are no valid items names for the menu") 
        break
    while True:
        confirm=input("What would you like another order?(y/n)\n: ") # THis is used if the user wants to go back to the menu. Also added conditions.
        if confirm=="y":
            print() # THis allows it to pass back to the first question.
            math()
            break
        elif confirm=="n":
            menu()
        else:
            print("Please enter a y or n")
def add_pass(add_account,password):
    ACC_PASS[add_account] = password

def login():# Asks for user age and the choice to login or add account
    global ACC_PASS
    while True: 
        try:
            age=int(input("Please enter your age:")) # Before doing so I added age boundaries between 13-18. 
            if age >18:
                print("You are not eligible")
            elif age >= 13: 
                print("You are eligible")
                break
            else:
                print("Your age must be between 13-18")
        except ValueError:
            print("Please enter an age")
    while True:
        print("Welcome to the BDSC Cafe app!")
        question=input("1. Add your school account\n2. Login\n:") # asking for the user to choose.
        if question=="1": 
            add_account = input("Enter the account name: ")# Asking user to enter an account name
            password = input("Enter password: ") # And password
            add_pass(add_account,password)
            print("Your password has been added.")
                
        elif question=="2": # This confirms if they have entered the correct username and password. 
            add_account=input("Enter account name: ")
            password=input("Enter the password: ")
            for i in ACC_PASS:
                if add_account==i and password==ACC_PASS[i]:# If the account passoword and name is in the dictionary
                    print("Login sucesss.")
                    menu()#It will open the menu.
            else:#Otherwise it will go back to the first input. 
                print("There are no passwords added for this account.")
        else:
            print("Please enter 1 out of the 3 numbers given.")  
login()
