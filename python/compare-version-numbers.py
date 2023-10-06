class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #insteads of this use
        # list1, list2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        def parse(ver:str)->list:
            return [int(k) for k in ver.split('.')]
        list1, list2 = parse(version1),parse(version2)
        i=0
        while i<len(list1) or i<len(list2):
            x = list1[i] if i < len(list1) else 0
            y = list2[i] if i < len(list2) else 0
            if x < y:
                return -1
            elif x > y:
                return 1
            i+=1
        return 0