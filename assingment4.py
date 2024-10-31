"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""
ib = float(input("Please enter the initial debt amount："))
ar = float(input("Please enter the annual interest rate (in decimals)："))
ap= float(input("Please enter the annual repayment amount："))


mr = ar/ 12
mp= ap/ 12

cd = ib
total= 0
months = 0


while cd> 0:
    interest_for_month = cd *mr 
    total+= interest_for_month

    cd += interest_for_month - mp

    months += 1

    if cd < 0:
        current_debt = 0
        break

print(f"{months} months")
print(f"Will pay {total:.2f} ")



