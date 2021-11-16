Shopping_cart=[]
sum = 0
add = True
print("Please add the items you have bought!")
value1 = input (">")
while not (value1.isnumeric()):
    print ("""Please add a correct value!
>""")
    value1 = input ()
good = int(value1)
Shopping_cart.append(good)
while add == True:
    print("""
Would you like to add something else?
    
Press 'y' for yes and 'n' for No
>""")
    answer = input()
    switch = True
    while switch != False:
        if answer == "y":
            add = True
            switch = False
            print("Please add the value of the next item!")
            value = input (">")
            while not (value.isnumeric()):
                print ("""Please add a correct value!
>""")
                value = input ()
            good = int(value)
            Shopping_cart.append(good)
        elif (answer != "y") and (answer != "n"):
            print("Please enter 'y' or 'n'!")
            answer = input()
        elif answer == "n":
            add = False
            switch = False
for item in Shopping_cart:
    sum = sum + item
print ("The sum is", sum, "$")