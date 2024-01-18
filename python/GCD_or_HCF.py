#optimal
#Euclidean’s algo
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(8,4))









#bruteforce sol

# take two numbers
# n1, n2 = 4, 8
# #store largest common number
# i=1
# #loop till min(n1,n2)
# for i in range(1,min(n1,n2)+1):
#   if n1 % i == 0 and n2 % i == 0:
#     ans = i
# print(ans)
