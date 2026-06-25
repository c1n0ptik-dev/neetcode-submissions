class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.ds.get(key)

        if arr == None:
            return ""

        n = len(arr) - 1

        l, h = 0, n

        while l <= h:
            mid = l + (h - l) // 2
            guess = arr[mid][1]

            if guess > timestamp:
                h = mid - 1
            
            elif guess < timestamp:
                l = mid + 1
            
            else:
                return arr[mid][0]
        
        return arr[h][0] if h >= 0 else ""

        

        

