def total_calc(bill_amount, tip_percent):
    total = bill_amount * (1 + tip_percent * 0.01)
    total = round(total, 2)

    return total

print("Total amount is:", total_calc(150, 20))