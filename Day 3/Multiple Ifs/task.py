print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 15
        print("Youth tickets are $7.")
    else:
        bill = 25
        print("Adults tickets are $12.")
        wants_photo = input("Would you like to see the picture? (y/n) ")
        if wants_photo == "y":
            #Add $3 to the bill
            bill += 3
        print(f"Your final bill  is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
