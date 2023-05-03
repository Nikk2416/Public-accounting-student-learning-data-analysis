# Import necessary functions from the "Input_Functions" module
from Input_Functions import get_capital,get_interest_rate,get_investment_period

# Prompt user for capital, interest rate, and investment period
capital = get_capital() # Prompt user for capital
interest_rate = get_interest_rate() # Prompt user for interest rate
investment_period = get_investment_period() # Prompt user for investment period

# Calculate the investment period in years
period_in_years = investment_period / 365

# Convert the interest rate from percentage to decimal
interest_rate_decimal = interest_rate / 100

# Calculate the total amount obtained and the interest earned
total_amount = round((capital * (1 + interest_rate_decimal * period_in_years)), 2) # Calculate total amount obtained
interest_earned = round((total_amount - capital), 2) # Calculate interest earned

# Display the results
print('--------------------------------------------------------------------------------------')
print(f'If you invest ${capital} in a fixed term deposit for {investment_period} days at an annual interest rate of {interest_rate}%,\nyou will get a total amount of ${total_amount}.\nThis means your investment earned you ${interest_earned} in interest.')

# Check if the investment was successful
if interest_earned > 0 and interest_earned >= (capital * 0.1):
    print(f'Excellent investment! You earned a profit of 10% or more on your investment.')
