# EXCEPTION:  An event that interrupts the flow of a program.

                # Types of Execution:
                                # ZeroDivisionError ( 1/0 )
                                # TypeError ( 1 + "1")
                                # ValueError ( int("pizza") )

                # Steps to overcome these error:
                        # try:   
                        #      some code 
                        # except Exception: 
                        #        Handle an Exception 
                        # finally: 
                        #        Do some clean up


# num = int(input("Enter a number: "))
# print(1 / num)

try: 
    num = input("Enter a number: ")
    print(1 / num)
except ZeroDivisionError:
    print("Kya aapne gareeb dekha h? nhi toh mirror dekho")      
except ValueError:
    print("Enter only number please! ")
except Exception:
    print("Something went wrong! ")
finally:
    print("Ho gya re baba")                      