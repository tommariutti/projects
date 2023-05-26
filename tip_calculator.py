print("Welcome to the tip calculator")

bill = (input("What was the total bill? "))

bill_float = float(bill)

percentage = input("What percentage tip would you like to give? ")

percentage_float = float(percentage)

number_people = input("How many people to split the bill? ")

number_people_float = float(number_people)

result = (bill_float / number_people_float) * (1 + (percentage_float / 100))

final_amount = round(result, 2)

print("The total amount is", final_amount, "and the tip is", result)

