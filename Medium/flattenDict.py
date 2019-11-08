class Solution(object):
    def DFS(self, nestedDict, keyNew):
        key = keyNew.split(".")[-1]
        if isinstance(nestedDict[key], dict):
            keySet = nestedDict[key].keys()
            for k in keySet:
                self.DFS(nestedDict[key], keyNew+"."+k)
        else:
            self.flattenDict[keyNew] = nestedDict[key]
        
    def flatten(self, nestedDict):
        keySet = nestedDict.keys()
        self.flattenDict = {}

        for k in keySet:
            self.DFS(nestedDict, k)

        return self.flattenDict

nestedD = {
    "a" : "100",
    "b" : "200",
    "c" : {
        "c1": "310",
        "c2": "320",
        "c3": "330",
        "c4": "340"
        },
    "d" : "400",
    "e" : "",
    "f" : {
        "f1" : {
            "f11":"1",
            "f12":"2",
            "f13": {
                "f1000": "1000"
            }
        },
        "f2": "500"
    },
    "g" : "600"
}

ob = Solution()
print (ob.flatten(nestedD))