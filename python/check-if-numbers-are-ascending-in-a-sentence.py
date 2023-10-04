class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        temp = s.split(" ")
        i=0
        prev = 0
        while i < len(temp):
            if temp[i].isdigit():
                print(temp[i])
                if int(temp[i]) > prev:
                    prev = int(temp[i])
                else:
                    return False
            i+=1
        return True


        