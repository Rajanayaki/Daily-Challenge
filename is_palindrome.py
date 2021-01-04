#O(N^2) TC
#O(N)
def ispalindrome(string):
    reversedstring=""
    for i in reversed(range(len(string))):
        reversedstring+=string[i]
    return reversedstring==string

string=input()
print(ispalindrome(string))

#O(N) TC
#O(N) SC
def ispalindrome(string):
    reversedstr=[]
    for i in reversed(range(len(string))):
        reversedstr.append(string[i])
    return "".join(reversedstr)==string

string=input()
print(ispalindrome(string))

#O(N) TC
#O(N) SC
def ispalindrome(string,i=0):
    j=len(string)-i-1
    return True if i>=j else string[i]==string[j] and ispalindrome(string,i+1)

string=input()
print(ispalindrome(string))

#O(N) TC
#O(N) SC
def ispalindrome(string,i=0):
    j=len(string)-i-1
    if i>=j:
        return True
    if string[i]!=string[j]:
        return False
    return ispalindrome(string,i+1)
string=input()
print(ispalindrome(string))

#O(N) TC
# O(1) SC
def ispalindrome(string):
    i=0
    j=len(string)-1
    while i<j:
        if string[i]!=string[j]:
            return False
        i+=1
        j-=1
    return True
string=input()
print(ispalindrome(string))
