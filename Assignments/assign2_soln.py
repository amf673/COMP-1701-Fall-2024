# COMP 1701 
# Fall 2024 
# Assignment 2 Soluion 
#

RATE = 0.014

def compute_retirement_income(avg_of_3_incomes: float, current_age: int, current_years_service: int, retirement_age: int) -> float:
    """
    calculates retirement income by applying the formula
    avg_of_3_incomes: the average of the 3 highest expected incomes over the person's career
    current_age: current age in years
    current_years_service: number of years of service currently
    retirement_age: age in years at retirement
    """
    years_service_at_retirement = (retirement_age - current_age) + current_years_service
    income = avg_of_3_incomes * RATE * years_service_at_retirement

    return income
    
#
# collect user inputs in this section
#

age = int(input("enter current age in years: "))
service_years = int(input("enter current years of service: "))
income1 = float(input('enter the largest expected annual income: '))
income2 = float(input('enter the second-largest expected annual income: '))
income3 = float(input('enter the third-largest expected annual income: '))

# perform processing and calculations in this section

avg_3_incomes = (income1 + income2 + income3) / 3
income_55 = compute_retirement_income(avg_3_incomes, age, service_years, 55)
income_60 = compute_retirement_income(avg_3_incomes, age, service_years, 60)
income_65 = compute_retirement_income(avg_3_incomes, age, service_years, 65)

# format and display output 

print(f'{"retirement age":20}{"retirement income":20}')
print(f'{55:<20}${income_55:<20,.2f}')
print(f'{60:<20}${income_60:<20,.2f}')
print(f'{65:<20}${income_65:<20,.2f}')
