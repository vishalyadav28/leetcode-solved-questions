#bruteforce
# n=10
# for i in range(0,n+1):
#     if n%i==0:
#         print(i)

#optimal 

n=36
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        print(i)
        if i!=(n/i):
            print(n/i)