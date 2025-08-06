def myfunc(income):

    income_tax = 0

    if income <= 10_000:
        income_tax = 0

    elif income <= 20_000:
        x = income - 10_000

        income_tax = x * 10 / 100
    else:
        
        #10 percent
        income_tax = 10_000 * 10 / 100

        # remaining
        income_tax += (income - 20_000) * 20 /100

    
    print(f'total income : {income}')
    print(f'total Taxable income : {income_tax}')

myfunc(19999)