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
initial_debt = float(input("请输入初始债务金额："))
annual_interest_rate = float(input("请输入年利率（以小数表示）："))
annual_payment = float(input("请输入年还款额："))

# 月度计算
monthly_interest_rate = annual_interest_rate / 12
monthly_payment = annual_payment / 12

current_debt = initial_debt
total_interest_paid = 0
months = 0

# 循环直到债务还清
while current_debt > 0:
    # 计算当前月的利息
    interest_for_month = current_debt * monthly_interest_rate
    total_interest_paid += interest_for_month

    # 更新当前债务：加上利息，减去还款
    current_debt += interest_for_month - monthly_payment

    # 增加月份计数
    months += 1

    # 如果债务还清，退出循环
    if current_debt < 0:
        current_debt = 0
        break

# 输出结果
print(f"{months} 个月")
print(f"他将支付 {total_interest_paid:.2f} 的利息")



