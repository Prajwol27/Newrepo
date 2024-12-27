#1


def price():
    a = float(input("Enter the price of iteam: "))
    if a>1000:
        b = a - (10/100)*a
        print(f"Your price is {b}.")
    elif a>500>=1000:
        b = a - (5/100)*a
        print(f"Your price is {b}.")
    else:
         print(f"Your price is {a}.")


#2
def food():
    a = str(input("Are you vegetarian or nonveg: "))
    a = a.casefold()
    if a == 'vegetarian':
        b = str(input("Do you want salad or pasta? : "))
        b = b.casefold()
        if b == 'salad':
            print("Here is your salad.")
        elif b == 'pasta':
            print('Here is your pasta.')
        else:
            print('Invalid input!!')
    elif a == 'nonveg':
        b = str("Do you want chicken or fish? : ")
        b == b.casefold()
        if b == 'chicken':
            print("Here is your chcken.")
        elif b == 'fish':
            print('Here is your fish.')
        else:
            print('Invalid input!!')
    else:
        print("Invalid input!!")



#3

def salary():
    a = float(input("Enter your salary: "))
    if a>50000:
        print("High Earner.")
    elif 20000<a<=50000:
        print("Mid-earner.")
    else:
        print("Low Earner.")



#4

def numb():
    a = int(input("Enter any integer: "))
    if a%2 == 0:
        if a%5==0:
            print(f"{a} is divisible by both 2 and 5.")
        else:
            print(f"{a} is only divisible by 2.")
    else:
        print(f"{a} is not divisible by both 2 and 5")



#5

def marks():
    a = float(input("Enter the marks of student: "))
    if 100>=a>90:
        print("Excellent")
    elif 51<=a<=90:
        print("Good")
    elif 0<a<51:
        print("Faild")
    else:
        print("Invalid input!!")


#6

def greatest():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    if a>b:
        if a>c:
            print(f"{a} is the greatest among all three.")
    elif b>a:
        if b>c:
            print(f"{b} is the greatest among all three.")
    elif c>a:
        if c>b:
            print(f"{c} is the greatest number of all.")
    else:
        print("All numbers are same.")



#7 

def game1():
    print("Welcome to Forest Adventure.")
    a = str(input("Choose a path 'left' or 'right': "))
    a = a.casefold()
    if a == 'left':
        b = str(input("Do you want to rest or explore? : "))
        b = b.casefold()
        if b == 'explore':
            print("You found a treasure!")
        else:
            print("You were attacked by wild animals. Game Over.")
    else:
        print("You went the wrong direction. Game over.")



#8

def game2():
    print("Welcome to Jungle Survival Challenge.")
    a = str(input