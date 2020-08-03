#O(N) TC
#O(N) SC
def caesarcipher(String,key):
    newletter=[]
    newkey=key%26
    alphabet=list("abcdefghijklmnopqrstuvwxyz")
    for letter in String:
        newletter.append(getnewletter(letter,newkey,alphabet))
    return "".join(newletter)

def getnewletter(letter,key,alphabet):
    newletter=alphabet.index(letter)+key
    return alphabet[newletter] if newletter<=25 else chr(alphabet[-1+newletter%25])

string=input()
key=int(input())
print(caesarcipher(string,key))
