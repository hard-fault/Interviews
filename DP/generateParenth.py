def validate(A):
    balance = 0
    for p in A:
        if p == '(': balance += 1
        else: balance -= 1
        if balance < 0: return False
    return balance == 0

def generate(A, n):
    if len(A) == 2*n:
        if validate(A):
            print A
    else:
        A.append('(')
        generate(A,n)
        A.pop()
        A.append(')')
        generate(A,n)
        A.pop()

def backTrack(A,left,right, n):
    if len(A) == 2*n:
        print A
    if left < n:
        A.append("(")
        backTrack(A, left+1, right,n)
    if right < left:
        A.append(")")
        backTrack(A, left, right+1,n)


    
A = []
n = 2

generate(A,n)
A = []
backTrack(A,0,0,n)