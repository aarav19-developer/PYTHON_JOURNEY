# DEFAULT ARGUMENTS:-
                   #  A default value for certain parameters.
                   #  Default is used when that argument is omitted make your functions more flexible, reduces number of arguments.

                   # 1. Positional argument
                   # 2. Default argument
                   # 3. Keywords argument
                   # 4. arbitrary argument

def net_price(list_price,discount,tax):
    return list_price*(1-discount)*(1+tax)

print(net_price(500,0,0.05))

import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("done!")
count(22,13)
    