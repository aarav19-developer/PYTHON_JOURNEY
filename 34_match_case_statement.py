# MATCH-CASE STATEMENT ( SWITCH ):-
                                 # An alternative to using many "elif" statements. 
                                 # Execute some code if a value matches a "case". 
                                 # Benefits: clearner and syntax is more readable.

def day_of_weeks(day):
    if day == 1:
        return "It is a Sunday"
    elif day == 2:
        return " It is Monday"
    elif day == 3:
        return " It is Tuesday"
    elif day == 4:
        return " It is Wednesday"
    elif day == 5:
        return " It is Thursday"
    elif day == 6:
        return " It is Friday"
    elif day == 7:
        return " It is Saturday"
    else:
        return 'It is not VALID'
    
print(day_of_weeks(2))

# INSTEAD OF IF AND ELSE WE CAN USE {MATCH AND CASE}

def day_of_weeks(day):
    match day:

     case 1:
        return "It is a Sunday"
     case 2:
        return " It is Monday"
     case 3:
        return " It is Tuesday"
     case 4:
        return " It is Wednesday"
     case 5:
        return " It is Thursday"
     case 6:
        return " It is Friday"
     case 7:
        return " It is Saturday"
     case _:
        return 'It is not VALID'
    
print(day_of_weeks(6))

