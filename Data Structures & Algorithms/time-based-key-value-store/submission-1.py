class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        if not values:
            return ""

        l = 0
        r = len(values)-1
        while l<r:
            m = (l+r)//2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return values[r][0]
        
        
