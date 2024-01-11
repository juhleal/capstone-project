import math

# Create a program that allows the user to choose between two different financial calculators.
# 1: investment calculator, 2: home loan repayment calculator .
# The user should be allowed to choose which calculation they want to do.

print("\n Investment = To calculate the amount of interest you'll earn on your investment.\n Bond       = To calculate the amount you'll pay on a home loan")

user_choice = input("\n Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Turning the output case insensitive:

user_choice = user_choice.lower()

# Asking the user additional informations:

if user_choice == "investment":

    deposit = float(input("\n Please enter the amount of money you are depositing: ")) 
    interest_rate = float(input("\n Please enter the interest rate (as a percentage) and only numbers: "))
    years = int(input("\n Please enter the number of years you plan to invest: ")) 
    interest = input("\n Please choose between 'simple' or compound' interest: ")

    interest = interest.lower() # Case insensitive

        # Using the formula "A = P *(1 + r * t), where:"
        # 'P' is deposit
        # 'r' is the interest_rate
        # 't' is the number of years the money will be invested
        # 'A' is the total amount after interest

    if interest == "simple":
        interest = deposit *(1 + (interest_rate / 100) * years)
        print("\n In {} years, you'll have £{} in your account.\n".format(years, interest))

        # Using the formula "A = P * math.pow(1 + r), t), where:"
        # 'P' is deposit
        # 'r' is the interest_rate
        # 't' is the number of years the money will be invested
        # 'A' is the total amount after interest

    elif interest == "compound":
        interest = deposit * math.pow((1 + (interest_rate / 100)), years)
        print("\n In {} years, you'll have £{} in your account.\n".format(years, interest))

    else:
        print("\n Error. Choose an appropriate option.")

elif user_choice == "bond":
    house_value = int(input("\n Please provide the present value of your house. e.g. 100000: "))
    interest_rate = float(input("\n Please enter the interest rate (as a percentage) and only numbers: "))
    months = int(input("\n Please provide the period (in monthts) that you plan to take to repay the bond. e.g. 120: "))
    
    # Using the formula "repayment = (1 * P)/(1 - (1 + i)**(-n))", where:
    # 'P' is house_value
    # 'i' is the interest_rate
    # 'n' is the number of months for repayment
    
    repayment = (((interest_rate / 100)/ 12) * house_value)/(1 - (1 + (interest_rate / 100)/ 12)**(-months))
    print("\n Your monthly repayment is: £{} to be paid in {} months. \n".format(repayment, months))

    # Or: repayment = (((interest_rate / 100)/ 12) * house_value)/(1 - math.pow(1 + ((interest_rate / 100)/12),-months))
     
else:
    print("\n Error. Choose an appropriate option.\n")

print("\n Thank you! \n")

# I had some difficulty in using "math.ceil" to round my float without turning into an integer. So I kept like that.
# I also tested the bond formula using "math.pow" and it worked the same.
# I also had a hard time trying to figure how to use a loop in case the user enters a different option, bringing back to the question.