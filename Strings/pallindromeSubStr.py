def getPallindromes(self,S):
    auxString = '@#' + '#'.join(S) + '#$'
    
    C = R = 0
    
    ## manachersTable is used to keep the count of pallindrome length seen so far.
    manachersTable = [0]*len(auxString)
    
    ##We make use of manachersTable to avoid repeated comparision, if the i exists in the current pallindrome centered around C.
    for i in range(1,len(auxString)-1):
        
        mirror = 2*C - i
        
        #If i is within the range of current pallindrome centered around C, use the mirror's count for a jump start.
        if i < R:
            manachersTable[i] = min(manachersTable[mirror], R-i)
        
        #Start expanding around the center
        while auxString[i+(1+manachersTable[i])]==auxString[i-(1+manachersTable[i])]:
            manachersTable[i] += 1
        
        #if i goes beyond the existing pallindrome centerd around C, then update.
        if i + manachersTable[i] > R:
            C = i
            R = i + manachersTable[i]
        
    for i in range(len(manachersTable)):
        manachersTable[i] = (manachersTable[i]+1)/2
        
    return sum(manachersTable)

def countSubstrings(self, S):
    if S == "":
        return [""]
    return self.getPallindromes(str(S))