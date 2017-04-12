#declaring variables
annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
sum_to_save = (portion_down_payment*total_cost - current_savings)#sum, that I have to save to buy a house
number_of_months = 0
#main part of problem
while current_savings <= sum_to_save:
    saved_this_month = current_savings*r/12 + portion_saved*monthly_salary
    current_savings += saved_this_month
    number_of_months += 1
print('Number of months:', number_of_months)
