class TwoSum:
    def __init__(self):
        self.numberHash = {}
    def add(self, number):
        self.numberHash[number] = 1

    def find(self, sum):
        keys = self.numberHash.keys()
        for k in keys:
            diff = sum - k
            if diff in keys:
                return True
        return False

obj = TwoSum()

obj.add(1)
obj.add(3)
obj.add(5)

print obj.find(4)
print obj.find(7)
