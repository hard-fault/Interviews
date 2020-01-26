import itertools

dict = {
    "2": ["a","b","c"],
    "3": ["d","e","f"],
    "4": ["g","h","i"],
    "5": ["j","k","l"],
    "6": ["m","n","o"],
    "7": ["p","q","r","s"],
    "8": ["t","u","v"],
    "9": ["w","x","y","z"]
}

def getText(num,index):
    if index < len(num) - 1:
        solution = list(itertools.product(dict[num[index]], getText(num,index+1)))
        for i in range(len(solution)):
            solution[i] = "".join(solution[i])
        return solution
    else:
        return dict[num[index]]


num = 232
num = list(str(num))
print getText(num,0)