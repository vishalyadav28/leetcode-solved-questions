# Basic idea behind solution

# n=10
# r=3
# res = 1
# for i in range(r):
#     res = res * (n-i)
#     res = res / (i+1)

# print(res)

#==============================================================>

#rough work

# trying but not good way 
# def cal_row(n,r):
#     res = 1
#     temp = []
#     for i in range(r):
#         res = res * (n-i)
#         res = res / (i+1)
#         temp.append(res)
#     return temp
       


# for c in range(5):
#     print(cal_row(10,3))



# n=10
# r=3
# res = 1
# for i in range(1,r):
#     res = res * (n-i)
#     res = res / (i)
#     print(res)

# print(res)


# result = []
# def nCr(n,c):
#     res = 1
#     temp = []
#     for k in range(1,n):
#         res = res * (n - c)
#         res = res // k
#         temp.append(res)
#     return temp


# for i in range(5):
#     data  = nCr(i,i)
#     result.append(data)

# print(result)

# print(nCr(4,2))

#=======================================================================================>


#naive

# n=5

# result = []
# def nCr(n, r):
#     res = 1

#     # calculating nCr:
#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)

#     return res

# for i in range(1,n+1):
#     temp = []
#     for j in range(1,i+1):
#         temp.append(nCr(i-1,j-1))
#     result.append(temp)


# print(result)


#optimized solution ================>

result = []
n=5

def nCr(row):
    ans = 1
    temp = [1]
    for col in range(1,row):
        ans *= (row - col)
        ans //= col
        temp.append(ans)
    return temp



for i in range(1,n+1):
    result.append(nCr(i))
print(result)

#===========================================>
