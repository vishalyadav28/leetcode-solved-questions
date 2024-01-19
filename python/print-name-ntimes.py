#1 way

# def print_name(n):
#     if n != 0: 
#         print("something")

#         print_name(n-1)
# print_name(5)



# other way 

def print_name(i,n):
    if i<n:
        print("------------name-----------")
        print_name(i+1,n)
print_name(0,5)