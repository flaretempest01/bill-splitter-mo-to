#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

bill = input("What was the total bill? ₱")

give_tip = input("would you like to give a tip? y/n ")

if give_tip == "y":
    tip = input(
        "How much tip would you like to give? 10, 12, or 15? (percentage) ")
elif give_tip not in ['y', 'n'] or give_tip == 'n':
    tip = 0

service_fee = input("is service fee included? y/n ")

if service_fee == "y":
    service_fee = input("How much is the service fee? ₱")
elif service_fee not in ['y', 'n'] or service_fee == 'n':
    service_fee = 0

people = input("How many people to split the bill? ")

bill_float = float(bill)
tip_float = float(tip)

service_fee_float = float(service_fee)
if service_fee == "y":
    service_fee_float = float(service_fee)
else:
    service_fee_float = 0

if give_tip == 'y':
    tip_percentage = tip_float / 100
else:
    tip_percentage = 0

people_int = int(people)
total_tip = bill_float * tip_percentage
total_bill = bill_float + total_tip + service_fee_float
bill_per_person = total_bill / people_int

final_amount = format(bill_per_person, ".2f")

print(f"Each person should pay: ₱{final_amount}")
