#TaskA
def valid_datatype(amount):
    try:
        amount = int(amount)
        return True
    except:
        return False
amount = input("Cost of groceries: ")
if valid_datatype(amount):
    amount = int(amount)
if not valid_datatype(amount):
    print("Wrong data type")
elif amount <= 0:
    print("Cost of groceries should be greater than £0")
elif amount < 10:
    print("Less than £10 (No coupon)")
elif amount <= 60:
    print(f"Awarded a discount coupon of £{amount * 8 / 100} (8% of purchase)")
elif amount <= 150:
    print(f"Awarded a discount coupon of £{amount * 9 / 100} (9% of purchase)")
elif amount <= 210:
    print(f"Awarded a discount coupon of £{amount * 10 / 100} (10% of purchase)")
else:
    amount = amount * 11 / 100
    if amount > 33:
amount = 33
        print(f"Awarded a discount coupon of £{amount} (capped)")
    else:
        print(f"Awarded a discount coupon of £{amount} (11% of purchase)")
#TaskB
def valid_datatype(amount):
    try:
        amount = int(amount)
        return True
    except:
        return False
total_amount = 0
total_discount = 0
no_coupon = 0
eight_per_coupon = 0
nine_per_coupon = 0
ten_per_coupon = 0
eleven_per_coupon = 0
while True:
    amount = input("Cost of groceries: ")
    if amount.lower() == "e":
        break
    if valid_datatype(amount):
        amount = int(amount)
        total_amount += amount
    if not valid_datatype(amount):
        print("Wrong data type")
    elif amount <= 0:
        print("Cost of groceries should be greater than £0")
    elif amount < 10:
        print("Less than £10 (No coupon)")
        no_coupon += 1
    elif amount <= 60:
        print(f"Awarded a discount coupon of £{amount * 8 / 100} (8% of purchase)")
        total_discount += (amount * 8 / 100)
        eight_per_coupon += 1
    elif amount <= 150:
        print(f"Awarded a discount coupon of £{amount * 9 / 100} (9% of purchase)")
        total_discount += (amount * 9 / 100)
        nine_per_coupon += 1
    elif amount <= 210:
        print(f"Awarded a discount coupon of £{amount * 10 / 100} (10% of purchase)")
        total_discount += (amount * 10 / 100)
        ten_per_coupon += 1
    else:
        amount = amount * 11 / 100
        if amount > 33:
            amount = 33
            print(f"Awarded a discount coupon of £{amount} (capped)")
            total_discount += 33
        else:
            print(f"Awarded a discount coupon of £{amount} (11% of purchase)")
            total_discount += amount

 eleven_per_coupon += 1
print(f"\nTotal groceries: {total_amount}\nTotal discount: {total_discount}\n"
+ f"Groceries - discount: {total_amount - total_discount}\n")
customers = no_coupon + eight_per_coupon + nine_per_coupon + ten_per_coupon + eleven_per_coupon
print("Histogram")
print("<£10 (0%)
print("£10-£60 (8%)
print("£61-£150 (9%)
print("£151-£210 (10%)  : " + ("*" * ten_per_coupon))
print(">£211 (11%/Cap)  : " + ("*" * eleven_per_coupon))
: " + ("*" * no_coupon))
: " + ("*" * eight_per_coupon))
: " + ("*" * nine_per_coupon))
print("\n" + f"{customers} customers")
#TaskC
def valid_datatype(amount):
    try:
        amount = int(amount)
        return True
    except:
        return False
total_amount = 0
total_discount = 0
no_coupon = 0
eight_per_coupon = 0
nine_per_coupon = 0
ten_per_coupon = 0
eleven_per_coupon = 0
while True:
    amount = input("Cost of groceries: ")
    if amount.lower() == "e":
        break
    if valid_datatype(amount):
        amount = int(amount)
        total_amount += amount
    if not valid_datatype(amount):
        print("Wrong data type")
    elif amount <= 0:
        print("Cost of groceries should be greater than £0")
    elif amount < 10:
        print("Less than £10 (No coupon)")
        no_coupon += 1
    elif amount <= 60:
        print(f"Awarded a discount coupon of £{amount * 8 / 100} (8% of purchase)")
        total_discount += (amount * 8 / 100)
        eight_per_coupon += 1
    elif amount <= 150:
        print(f"Awarded a discount coupon of £{amount * 9 / 100} (9% of purchase)")
        total_discount += (amount * 9 / 100)
        nine_per_coupon += 1
    elif amount <= 210:
        print(f"Awarded a discount coupon of £{amount * 10 / 100} (10% of purchase)")
        total_discount += (amount * 10 / 100)
        ten_per_coupon += 1
    else:
        amount = amount * 11 / 100
        if amount > 33:
            amount = 33
            print(f"Awarded a discount coupon of £{amount} (capped)")
            total_discount += 33
        else:
            print(f"Awarded a discount coupon of £{amount} (11% of purchase)")
            total_discount += amount
        eleven_per_coupon += 1
print(f"\nTotal groceries: {total_amount}\nTotal discount: {total_discount}\n"
+ f"Groceries - discount: {total_amount - total_discount}\n")
customers = no_coupon + eight_per_coupon + nine_per_coupon + ten_per_coupon + eleven_per_coupon
print("Histogram")
print("<£10 (0%)
print("£10-£60 (8%)
print("£61-£150 (9%)
print("£151-£210 (10%)  : " + ("*" * ten_per_coupon))
print(">£211 (11%/Cap)  : " + ("*" * eleven_per_coupon))
print("\n" + f"{customers} customers")
print("\n0%   8%   9%   10%  11%")
while True:
    if no_coupon > 0:
        print(" *   ", end="")
: " + ("*" * no_coupon))
: " + ("*" * eight_per_coupon))
: " + ("*" * nine_per_coupon))

         no_coupon -= 1
    else:
        print("     ", end="")
    if eight_per_coupon > 0:
        print(" *   ", end="")
        eight_per_coupon -= 1
    else:
        print("     ", end="")
    if nine_per_coupon > 0:
        print(" *   ", end="")
        nine_per_coupon -= 1
    else:
        print("     ", end="")
    if ten_per_coupon > 0:
        print(" *   ", end="")
        ten_per_coupon -= 1
    else:
        print("     ", end="")
    if eleven_per_coupon > 0:
        print(" *   ")
        eleven_per_coupon -= 1
    else:
print(" ")
    if no_coupon <= 0 and eight_per_coupon <= 0 and nine_per_coupon <= 0 and ten_per_coupon <= 0 and eleven_per_coupon <= 0:
        break
#TaskD
from dis import dis
def valid_datatype(amount):
    try:
        amount = int(amount)
        return True
    except:
return False
total_amount = 0
total_discount = 0
no_coupon = 0
eight_per_coupon = 0
nine_per_coupon = 0
ten_per_coupon = 0
eleven_per_coupon = 0
min_groceries = 500000
max_groceries = 0
min_discount = 5000000
max_discount = 0
while True:
    amount = input("Cost of groceries: ")
    coupon = 0
    if amount.lower() == "e":
        break
    if valid_datatype(amount):
        amount = int(amount)
        if amount < min_groceries:
            min_groceries = amount
        if amount > max_groceries:
            max_groceries = amount
        total_amount += amount
    if not valid_datatype(amount):
        print("Wrong data type")
    elif amount <= 0:
        print("Cost of groceries should be greater than £0")
    elif amount < 10:
        print("Less than £10 (No coupon)")
        no_coupon += 1
    elif amount <= 60:
        coupon = amount * 8 / 100
        print(f"Awarded a discount coupon of £{coupon} (8% of purchase)")
        total_discount += coupon
        eight_per_coupon += 1
    elif amount <= 150:
        coupon = amount * 9 / 100
        print(f"Awarded a discount coupon of £{coupon} (9% of purchase)")
        total_discount += coupon
        nine_per_coupon += 1
    elif amount <= 210:
        print(f"Awarded a discount coupon of £{coupon} (10% of purchase)")
        coupon = amount * 10 / 100
        total_discount += coupon

         ten_per_coupon += 1
    else:
        coupon = amount * 11 / 100
        if coupon > 33:
            coupon = 33
            print(f"Awarded a discount coupon of £{coupon} (capped)")
            total_discount += 33
        else:
            print(f"Awarded a discount coupon of £{coupon} (11% of purchase)")
            total_discount += coupon
        eleven_per_coupon += 1
    if coupon > max_discount:
        max_discount = coupon
    if coupon < min_discount:
        min_discount = coupon
print(f"\nTotal groceries: {total_amount}\nTotal discount: {total_discount}\n"
+ f"Groceries - discount: {total_amount - total_discount}\n")
print(f"Minimum groceries: {min_groceries}\nMaximum groceries: {max_groceries}"
+ f"\nMinimum coupon: {min_discount}\nMaximum coupon: {max_discount}")
customers = no_coupon + eight_per_coupon + nine_per_coupon + ten_per_coupon + eleven_per_coupon
print("\nHistogram")
print("<£10 (0%)
print("£10-£60 (8%)
print("£61-£150 (9%)
print("£151-£210 (10%)  : " + ("*" * ten_per_coupon))
print(">£211 (11%/Cap)  : " + ("*" * eleven_per_coupon))
: " + ("*" * no_coupon))
: " + ("*" * eight_per_coupon))
: " + ("*" * nine_per_coupon))
print("\n" + f"{customers} customers")
print("\n0%   8%   9%   10%  11%")
while True:
    if no_coupon > 0:
        print(" *   ", end="")
        no_coupon -= 1
    else:
        print("     ", end="")
    if eight_per_coupon > 0:
        print(" *   ", end="")
        eight_per_coupon -= 1
    else:
        print("     ", end="")
    if nine_per_coupon > 0:
        print(" *   ", end="")
        nine_per_coupon -= 1
    else:
        print("     ", end="")
    if ten_per_coupon > 0:
        print(" *   ", end="")
        ten_per_coupon -= 1
    else:
        print("     ", end="")
    if eleven_per_coupon > 0:
        print(" *   ")
        eleven_per_coupon -= 1
    else:
print(" ")
    if no_coupon <= 0 and eight_per_coupon <= 0 and nine_per_coupon <= 0 and ten_per_coupon <= 0 and eleven_per_coupon <= 0:
        break
#TaskE
def valid_datatype(amount):
    try:
        amount = int(amount)
        return True
    except:
        return False
list = [10, 14, 58, 62, 200, 8, 512]
total_amount = 0
total_discount = 0
no_coupon = 0
eight_per_coupon = 0
nine_per_coupon = 0
ten_per_coupon = 0
eleven_per_coupon = 0

 for amount in list:
    if valid_datatype(amount):
        amount = int(amount)
        total_amount += amount
    if not valid_datatype(amount):
        print("Wrong data type")
    elif amount <= 0:
        print("Cost of groceries should be greater than £0")
    elif amount < 10:
        print("Less than £10 (No coupon)")
        no_coupon += 1
    elif amount <= 60:
        print(f"Awarded a discount coupon of £{amount * 8 / 100} (8% of purchase)")
        total_discount += (amount * 8 / 100)
        eight_per_coupon += 1
    elif amount <= 150:
        print(f"Awarded a discount coupon of £{amount * 9 / 100} (9% of purchase)")
        total_discount += (amount * 9 / 100)
        nine_per_coupon += 1
    elif amount <= 210:
        print(f"Awarded a discount coupon of £{amount * 10 / 100} (10% of purchase)")
        total_discount += (amount * 10 / 100)
        ten_per_coupon += 1
    else:
        amount = amount * 11 / 100
        if amount > 33:
            amount = 33
            print(f"Awarded a discount coupon of £{amount} (capped)")
            total_discount += 33
        else:
            print(f"Awarded a discount coupon of £{amount} (11% of purchase)")
            total_discount += amount
        eleven_per_coupon += 1
print(f"\nTotal groceries: {total_amount}\nTotal discount: {total_discount}\n"
+ f"Groceries - discount: {total_amount - total_discount}\n")
customers = no_coupon + eight_per_coupon + nine_per_coupon + ten_per_coupon + eleven_per_coupon
print("Histogram")
print("<£10 (0%)
print("£10-£60 (8%)
print("£61-£150 (9%)
print("£151-£210 (10%)  : " + ("*" * ten_per_coupon))
print(">£211 (11%/Cap)  : " + ("*" * eleven_per_coupon))
print("\n" + f"{customers} customers")
: " + ("*" * no_coupon))
: " + ("*" * eight_per_coupon))
: " + ("*" * nine_per_coupon))