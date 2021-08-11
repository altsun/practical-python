# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    if month in range(extra_payment_start_month, extra_payment_end_month + 1):
        actual_payment = payment + extra_payment
    else:
        actual_payment = payment
    new_principal = principal * (1+rate/12) - actual_payment
    if new_principal < 0:
        actual_payment = principal
        principal = 0
    else:
        principal = new_principal
    total_paid = total_paid + actual_payment
    print(month, total_paid, principal)

print(f'Total paid {total_paid}')
print(f'Months {month}')