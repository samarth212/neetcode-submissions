class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[(key, timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.timeMap:
            return self.timeMap[(key, timestamp)]
        for time in range(timestamp, -1, -1):
            if (key, time) in self.timeMap:
                return self.timeMap[(key, time)]
        return ""
        
