 
# MT 2 Fall 24
# 
# Tax Payable

# 3 marks for constants 
DEPENDENT_AMT_1 = 5000.00
DEPENDENT_AMT_2 = 4000.00
DEPENDENT_AMT_3 = 3500.00
TAX_CUTOFF      = 20000.00
TAX_RATE        = 0.20

# 4 marks for calculation should be in function but could be
# in the other function 
def dependent_deduction( dependents:int)->float: 
    """ Calculate the deduction for dependents. """
    
    if dependents <= 0: 
        deduction = 0.0 
    elif dependents == 1:
        deduction = DEPENDENT_AMT_1
    elif dependents == 2:
        deduction = DEPENDENT_AMT_2 * dependents
    else:
        deduction = DEPENDENT_AMT_3 * dependents

    return deduction
    
# 3 mark for header and hints and docstring 
def taxable_income( total_income: float, dependents:int)-> float:
    """ return the taxable income""" 
    
    return (total_income - dependent_deduction(dependents))

def tax_owing( income: float, dependents:int) -> float:
    """ Calculate the amount owing on taxable_income """

    taxable_income = taxable_income( income, dependents)
    if taxable_income > TAX_CUTOFF:
        owing = (taxable_income - TAX_CUTOFF) * TAX_RATE
    else: 
        owing = 0.0
    
    # 2 marks for 1 and only 1 return 
    return owing

def main()->None:
    """ Taxable Income calculator """
    # 2 mark for output format 
    print("\nTax Calculator 1.0\n")
    
    # 1 mark for input 
    income = float(input("Enter the total income in $: "))
    deps = int(input("Enter the number of dependents: "))

    # 1 mark for function call 
    owing = tax_owing(income, deps)
    
    print(f"The tax owing on ${income:,.2f} with {deps} dependents is ${owing:,.2f} ")

main()

# 1 mark for main
