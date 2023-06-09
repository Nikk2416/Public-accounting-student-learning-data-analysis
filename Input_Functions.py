# Create a function to request the capital, preventing incorrect data entry
def get_capital():
    while True:
        Capital_to_invest = input('Please enter the capital you are going to invest: ')
        try:
            Capital_to_invest = float(Capital_to_invest)
        except: 
            print('You must enter a number!')
        else:
            break
    return Capital_to_invest

# Create a function to request the interest rate, preventing incorrect data entry and must be between (0;100]
def get_interest_rate():
    while True:
        nominal_interest_rate = input('Please enter the nominal interest rate as a percentage: ')
        try: 
            nominal_interest_rate = float(nominal_interest_rate) 
        except: 
            print('Please enter the interest rate again, it must be a percentage between 0 and 100') 
        else: 
            if 0 < nominal_interest_rate <= 100:
                break
            else: 
                print('Please enter the interest rate again, it must be a percentage between 0 and 100')
    return nominal_interest_rate

# Create a function to request the number of days, preventing incorrect data entry and must be greater than 0
def get_investment_period():
    while True:
        number_of_days = input('Please enter how many days your investment will last: ')
        try: 
            number_of_days = int(number_of_days)
        except:
            print('You must enter a number of days!')
        else:
            if number_of_days > 0:
                break
            else: 
                print('You must enter a number of days!')
    return number_of_days
