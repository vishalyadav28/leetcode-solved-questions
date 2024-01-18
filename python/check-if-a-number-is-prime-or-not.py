
#Bruteforce

# def prime_or_not(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# print(prime_or_not(n = 6))



#optimal

def prime_or_not(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(prime_or_not(n =11))