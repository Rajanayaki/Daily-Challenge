#O(N) TC
#O(N) SC
def ispalindrome(string):
    reversedstr=[]
    for i in reversed(range(len(string))):
        reversedstr.append(string[i])
    return "".join(reversedstr)==string

string=input()
print(ispalindrome(string))
