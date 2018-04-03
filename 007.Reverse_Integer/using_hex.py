# Inspired by this answer in Stack Overflow: https://stackoverflow.com/questions/44581339/reverse-32bit-integer

# The limits are −2,147,483,648 and 2,147,483,647. The hex values of them are -0x80000000 and 0x7fffffff.
# You can see that, for positive values: 
# 2147483647 & 0x7fffffff = 2147483647; 1 & 0x7fffffff = 1; 780 & 0x7fffffff = 780
# where '&' is the 'bitwise AND' operator.
# That is, for values within the limit, the value is given as output.
# And:
# 2147483648 & 0x7fffffff = 0; 98989898989898 & 0x7fffffff = 1640235338
# That is, for values exceeding the limit, some other value is displayed.

# For negative values:
# -2147483648 & -0x80000000 = -2147483648; -2147483647 & -0x80000000 = -2147483648; -2 & -0x80000000 = -2147483648
# That is, for values within the limit, the limit is given as output.
# And:
# -2147483649 & -0x80000000 = -4294967296; -999999999999 & -0x80000000 = -1000727379968
# That is, for values exceeding the limit, some other value is displayed.

# We can use this to solve the problem.


class Solution:
    def reverse(self, x):
        self.x = str(x)
         
        if x >= 0 and (int(self.x[::-1]) & 0x7fffffff == int(self.x[::-1])):
            return int(self.x[::-1])
        elif x < 0 and (-int(self.x[:0:-1]) & -0x80000000 == -0x80000000):
            return -int(self.x[:0:-1])
        else:
            return 0
