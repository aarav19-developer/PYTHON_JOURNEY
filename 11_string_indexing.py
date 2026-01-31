# INDEXING:- accessing elements of a sequence using [] (indexing opeartor).
           # [start : end : step]

credit_number = "1234 - 6765 - 1322 - 0806"
print(credit_number[:10:2])
print(credit_number[:-10:2])
print(credit_number[::2])
print(credit_number[-5:]) # last four digits.
print(credit_number[::-1])  # revesing the digits




# FORMAT SPECIFIERS:- { value : flags} format a value based on what flags are inserted.

# .(number)f = round to that many decimal places(fixed place).
# :(number) = allocate that many spaces.
# :03 = allocate and zero pad that many spaces.
# :< = left justify.
# :> = right justify.
# :^ = center justify.
# :+ = use a plus sign to indicate position value.
# := = place sign to leftmost position.
# : = insert a space before positive numbers.
# :, = comma separator.

price1 = 3.14597
price2 = -425.987
price3 = 12.65

print(f"Price 1 is ${price1:.1f}")
print(f"Price 1 is ${price1:10}")
print(f"Price 1 is ${price1:0010}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:^10}")