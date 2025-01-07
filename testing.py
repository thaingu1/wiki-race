import math
import time
import random
## print("I will calculate the area of a rectangle")

   ## units = input("What units are you using? ")

    ## width = int(input("What is the width of the rectangle? "))

   ## length = int(input("What is the length of the rectangle? "))

   ## area = width * length
   ## print(f"The area of the rectangle is {area} {units}²")
"""
num1 = int(input("Enter the first number: "))
op = input("enter the operation (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

if op == "/":
    result = num1 / num2
    print(round(result,3))
elif op == "*":
    result = num1 * num2
    print(round(result,3))
elif op == "+":
    result = num1 + num2
    print(round(result,3))
elif op == "-":
    result = num1 - num2
    print(round(result,3))


principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the inital principle: "))
    if principle <= 0:
        print(" principle must be greater than 0")
while rate <= 0 or rate > 1:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0 or rate > 1:
        print(" rate must be greater than 0 and less than 1")
while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print(" time must be greater than 0")

result = principle * pow((1 + rate), time)
print (f"after {time} years, your principle of ${principle} is worth ${result:.2f}")


timer = int(input("How long do you want to count down for? "))

for x in range(timer,0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("TIMES UP!")


fruits = ("Apple", "Banana", "Kiwi")
print(fruits[1])


Inventory = {"Banana": "1.25",
             "Pizza": "10.00",
             "Cookie": "2.00",
             "T-shirt": "7.50"}

item = input("What would you like to buy? ")
total = 0.0
keys = Inventory.keys()
while True:
    if Inventory.get(item):
        total += float(Inventory.get(item))
    else:
        print("We do not have that item, here is our inventory:")
        for key in keys:
            print(key)
    done = input("Are you done shopping? (Y/N) ")
    if done == "Y":
        break
    else:
        item = input("What else would you like to buy? ")

print(f"Your total is ${total}")

x = random.randint(0,100)

print(x)


low = 1
high = 1000
answer = random.randint(low, high)
guesses = 0
running = True
max_guesses =  math.ceil(math.log2(high - low))

print("Python Number Guessing Game")
print("-----------Rules-----------")
print(f"1. The number is between {low} and {high}")
print("2. lowest number of guesses wins")
print(f"3. the maximum number of guesses is {max_guesses}")

while running and guesses < max_guesses:
    guesses += 1
    guess = int(input(f"Enter guess number {guesses}: "))
    

    if guess == answer:
        running = False
    elif guess < answer:
        print("Your guess is too low")
    elif guess > answer: 
        print("Your guess is too high ")

if guesses < max_guesses:
    print("CORRECT!! You guessed the number!")
    print(f"It took you {guesses} guesses")
else:
    print("You failed :(")
  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = [num for num in numbers if num % 2 == 0]

print (even_nums)
  """
members = {"thaingu" : 1000, "hirongu": 500}

#print(type(members.get("thaingu")))


def register (user):
    members[user] = 0

def show_balance (username):
    if  username in members:
        print (f"{username} has a balance of ${members.get(username):.2f}")
    else:
        print("username not found")

def deposit(username, amt):
    if  username in members:
        members[username] += float(amt)
        print (f"{username} now has a balance of ${members.get(username):.2f}")
    else:
        print("username not found")

def withdraw(username, amt):
    if  username in members:
        members[username] -= float(amt)
        print (f"{username} now has a balance of ${members.get(username):.2f}")

    else:
        print("username not found")

while True:
    print("Python Bank")
    print("1. register new user")
    print("2. show balance")
    print("3. deosit")
    print("4. withdraw")
    print("q to quit")
    action = input("What would you like to do? ")
    if action == "q":
        break

    match action:
        case "1":
            register(input("Enter account username: "))
            print("-----------")
        case "2":
            show_balance(input("Enter account username: "))
            print("-----------")
        case "3":
            user = input("Enter account username: ")
            ammount = float(input("Enter ammount to deposit: "))
            deposit(user, ammount)
            print("-----------")
        case "4":
            user = input("Enter account username: ")
            ammount = float(input("Enter ammount to withdraw: "))
            withdraw(user, ammount)
            print("-----------")
        case _: 
            print("Enter a valid action")
            print("-----------")
    input("press enter to continue")

    

        


