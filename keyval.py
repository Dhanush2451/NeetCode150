class TimeMap:

    def __init__(self):
        self.keyStore={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key]={}
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp]=[]
        self.keyStore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        s=0
        for time in self.keyStore[key]:
            if time<=timestamp:
                s=max(s,time)
        return "" if s == 0 else self.keyStore[key][s][-1]
