
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
ticket = 0

if height >=120:
    print("You can ride")
    age = int(input("What is your age in years?"))
    if age >= 45:
        print("Everything will be OK, have a free ride on us!")
    elif age > 18:
        ticket = 12
        print("Adult tickets are 12 euro.")
    elif age >= 12:
        ticket = 7
        print("Youth tickets are 7 euro.")
    else:
        ticket = 5
        print("Child tickets are 5 euro.")

    photo = input("Do you want a photo?")
    if photo == "yes":
        ticket = ticket + 3
    
    print(f"Your final ticket is {ticket}")

else:
    print("Your have to grow taller!")


