#O(N) TC
#O(N) SC
def caesarcipher(string,key):
    newLetters=[]
    newKey=key%26
    for letter in string:
        newLetters.append(getnewletter(letter,key))
    return "".join(newLetters)0

def getnewletter(letter,key):
    newlettercode=ord(letter)+key
    return chr(newlettercode) if newlettercode<=122 else chr(96+newlettercode%122)
string=input()
key=int(input())
print(caesarcipher(string,key))
