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
