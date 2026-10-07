class TimeMap:

    def __init__(self):
       self.dicts = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dicts:
            self.dicts[key].append((timestamp, value))
        else:
           self.dicts[key] = [(timestamp, value)] 
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dicts:
            values = self.dicts[key]
            res = ""

            l = 0
            r = len(values)-1

            while l <= r:
                m = (l + r) // 2

                if values[m][0] <= timestamp:
                    res = values[m][1]
                    l = m + 1
                else:
                    r = m - 1
            
            return res
        
        return ""

         
