def armstrong_number(n):
    #for finding len of number
    org = n
    power=0
    while n!=0:
        n=n//10
        power+=1
    #now find is it armstrong
    temp2 = org
    result = 0
    while temp2!=0:
        result += (temp2%10)**power
        temp2 //= 10
    return result == org

print(armstrong_number(170))


# def is_armstrong(number):
#     digits = [int(digit) for digit in str(number)]
#     n = len(digits)
#     total = sum(digit ** n for digit in digits)
#     return total == number