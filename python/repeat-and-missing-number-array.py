def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your code here
    frequency = {i:0 for i in range(1,len(a)+1)}
    for number in a:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
    key = 0
    value = 0

    for k,v in frequency.items():
        if k!=0:
            if v==2:
                key = k
            if v==0:
                value = k
    return [key,value]