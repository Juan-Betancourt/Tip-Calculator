#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calulator!")
bill = input("What was the total bill? \n""$" )
tip = input("How much tip would you like to give? 15, 18, or 20? \n")
split_bill = input("How many people will split in this bill? \n")

total_bill = float(bill)
number_conver_of_tip = int(tip)
conver_of_split_bill = int(split_bill)

calculation_of_tip = (number_conver_of_tip / 100 * total_bill + total_bill )

final_bill = (calculation_of_tip / conver_of_split_bill)

print("\n The final bill for each individual is ${:0.2f} \n".format(final_bill))







#print("Welcome to the tip calculator!")
#bill = float(input("What was the total bill? $"))
#tip = int(input("How much tip would you like to give? 15, 18, or 20? "))
#people = int(input("How many people to split the bill? "))

#tip_as_percent = tip / 100
#tip_amount = bill * tip_as_percent
#total_bill = bill + tip_amount
#bill_per_person = total_bill / people
#final_amount_per_person = round(bill_per_person, 2)
#final_amount_per_person = "{:.2f}".format(bill_per_person)

#print (f"Each person should pay: ${final_amount_per_person}")



#print (bill_total_tip)