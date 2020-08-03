#O(N^2) TC
#O(N)
def ispalindrome(string):
    reversedstring=""
    for i in reversed(range(len(string))):
        reversedstring+=string[i]
    return reversedstring==string

string=input()
print(ispalindrome(string))
