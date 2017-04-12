def sign(a):
    if a > 0:
        i = 1
    if a < 0:
        i = -1
    else:
        i = 0
    return i
total_cost = 1000000
portion_down_payment = 0.25
sum_to_save = (portion_down_payment*total_cost)
annual_salary = int(input('Enter the starting salary: '))
def savings_for_36_month(annual_salary, portion_saved):
    r = 0.04
    current_savings = 0
    semi_annual_raise = 0.07
    monthly_salary = annual_salary/12
    number_of_months = 0
    current_savings = 0
    while number_of_months < 36:
        saved_this_month = current_savings*r/12 + portion_saved*monthly_salary
        current_savings += saved_this_month
        number_of_months += 1
        if number_of_months%6 == 0:
            monthly_salary += monthly_salary*semi_annual_raise
    return current_savings
portion_saved_1 = 0
portion_saved_2 = 1
steps = 0
maximum_saved = savings_for_36_month(annual_salary, portion_saved_2)
if maximum_saved < sum_to_save:
    print ('It is not possible to pay the down payment in three years.')
else:
    while True:
        steps +=1
        portion_saved_M = (portion_saved_1 + portion_saved_2)/2
        total_cost_saved_1 = savings_for_36_month(annual_salary, portion_saved_1)
        total_cost_saved_2 = savings_for_36_month(annual_salary, portion_saved_2)
        total_cost_saved_M = savings_for_36_month(annual_salary, portion_saved_M)
        if  abs(sum_to_save - total_cost_saved_M) < 100:
            print('Beat savings rate: ', portion_saved_M)
            print('Beat savings rate: {0:6.4f}'.format(portion_saved_M))
            print('Steps in bisection search: ',steps)
            break
        elif sign(sum_to_save - total_cost_saved_1) != sign(sum_to_save - total_cost_saved_M) < 0:
            portion_saved_2 = portion_saved_M
        else:
            portion_saved_1 = portion_saved_M

     
