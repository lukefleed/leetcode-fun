#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/Jnb6MBB.png)

# In[3]:


def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    res = []
    if numerator * denominator < 0: # if the result is negative
        res.append("-")
    numerator = abs(numerator)
    denominator = abs(denominator)
    res.append(str(numerator // denominator))
    remainder = numerator % denominator 
    if remainder == 0: # if the result is an integer
        return "".join(res)
    res.append(".") # if the result is a decimal
    dic = {} # key: remainder, value: index
    while remainder != 0: # if the result is a repeating decimal
        if remainder in dic: # if the remainder is repeating
            res.insert(dic[remainder], "(") # insert "(" at the index of the first remainder
            res.append(")") # append ")" at the end
            break # break the loop
        dic[remainder] = len(res) # add the remainder and its index to the dictionary
        remainder *= 10 # multiply the remainder by 10 to get the next digit
        res.append(str(remainder // denominator)) # append the next digit to the result
        remainder %= denominator # get the new remainder for the next iteration
    return "".join(res) 
    

