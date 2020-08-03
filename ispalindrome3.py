#O(N) TC
#O(N) SC
def ispalindrome(string,i=0):
    j=len(string)-i-1
    return True if i>=j else string[i]==string[j] and ispalindrome(string,i+1)

string=input()
print(ispalindrome(string))
