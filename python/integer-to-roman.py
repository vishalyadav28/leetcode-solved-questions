class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        result_string = ""
        for i in range(len(values)-1,-1,-1):
            while num >= values[i]:
                result_string+=romans[i]
                num-=values[i]
        return result_string

        
        