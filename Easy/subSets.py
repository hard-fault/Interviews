from itertools import chain, combinations

def getAllSubsets(value):
	allSubsets = []
	for i in range(len(value)):
		subset = list(combinations(value,i))
		for s in subset:
			allSubsets.append(s)
	return allSubsets

a = "GeeksforGeeks"
print getAllSubsets(a)

