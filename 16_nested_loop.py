# # NESTED-LOOP:- A loop withinanother loop ( outer, inner)
#                 # outer loop:
# #                      inner loop:

# for i in range(0,10):
#     print(i, end = "")

# for i in range(3):
#     for j in range(0,10):
#         print(j, end = "") # end is use to align the data in single line.
#     print() # ye use hota h jisse hmara data alag alag line m aa jaye.

# # TASK:
# # Print a rectangle using any symbol.

# rows = int(input("enter the number of rows: "))
# column = int(input("enter the number of column: "))
# symbol = (input("enter the symbol: "))
# for x in range(rows):
#     for y in range(column):
#         print(symbol, end="")
#     print()