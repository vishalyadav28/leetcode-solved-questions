def countDigits(n: int) -> int:
    # Write your code here
    #sol 1
    # count=0
    # while n != 0:
    #     n = n // 10 
    #     count+=1
    # return count
    #sol 2
    return len(str(n))
