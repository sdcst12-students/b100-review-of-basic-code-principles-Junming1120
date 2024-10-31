"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

P = float(input("Enter an intial investment: "))
r = float(input("Enter the annual interest rate in percentage: "))
x = input("Enter in date(d) / year(y) or month(m): ")
if x == "d":
  t = int(input("Enter number of days: "))
  t = t/365
elif x == "y":
  t = int(input("Enter number of years: "))
elif x == "m":
  t = int(input("Enter number of months: "))
  t = t/12
else:
  print("Somethings wrong")
I = P * r / 100 * t
I = round(I,2)
print(f"The amount of simple interest for your investment is ${I}")