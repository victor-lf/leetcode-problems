# The reversed integer must be within the 32-bit signed integer range. That is, it must be between 
# −2,147,483,648 (−2^31) and 2,147,483,647 (2^31 − 1) 


def reverse(x):
    str_x = str(x)
    
    if x >= 0 and int(str_x[::-1]) <= (2**31-1):
        return int(str_x[::-1])
    elif x < 0 and -int(str_x[:0:-1]) >= (-2**31):
        return -int(str_x[:0:-1])
    else:
        return 0
