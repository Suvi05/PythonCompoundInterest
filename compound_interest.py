# estimated final value of a monthly investment

print('How many years will you be investion?')
years = int(input('Enter years: '))

print('How much money is currently in your investment account?')
principal = float(input('Enter the current amount in your acount: '))

print('How much money do you plan on investing monthly?')
monthly_invest = float(input('Enter amount: '))

print('What do you estimate will be the yearly interest of this investment?')
interest = float(input('Enter your estimated interest in decimal numbers (10% = 0.1): '))

print(' ')

final_amount = 0

for i in range(0, years*12):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interest/12)

print('After {} years you will have '.format(years) + "${:,.2f}".format(final_amount))