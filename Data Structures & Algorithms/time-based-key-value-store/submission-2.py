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
        res = ""

        while l<=r:
            m = (l+r)//2
            value, time = values[m]
            if time == timestamp:
                return value
            elif time < timestamp:
                l = m + 1
                res = value
            else:
                r = m - 1
        return res
        
        
