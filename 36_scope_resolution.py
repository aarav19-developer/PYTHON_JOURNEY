#  VARIABLE SCOPE:-
                   # where a variable is visible and accessible.
# SCOPE RESOLUTION:-
                   # (LEGB) Local -> Enclosed -> Global -> Built-in.

# def func1():
#     a = 1
#     print(b)

# def func2():
#     b = 2
#     print(a)

# func1()
# func2()

#------------------------NXT ONE-------------------#

# if __name__ == __main__:-
                          # ( This sript can be imported OR run stand alone)
                          # Functions and classes in this module can be reused 
                          # without the main block of code executing.

                    # Good practice ( code is modular, helps readability, leaves no global variables, avoid unintended execution)
                        # Ex- library = import library for functionality 
                        # when running library directly, display a help page.


def main():
    # Your program goes here
 if  __name__ == '__main__':
    main() 

#------------------------NXT ONE-------------------#
print(dir()) 


#------------------------NXT ONE-------------------#
def favourite_food(food):
  print(f"Your favourite food is {food}")

def main():
  print("This is script1")
  favourite_food("Apple")
  print("Goodbye")

if __name__ =='__main__':
  main()


#------------------------NXT ONE-------------------#

def favourite_drink(drink):
  print(f"Your favourite drink is {drink}")

def main():
  print("This is script2")
  favourite_drink("sikanji")
  print("goodbye")

if __name__ == '__main__':
  main()

