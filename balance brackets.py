def balancebrackets(string):
    openingbrackets="{[("
    closingbrackets=")]}"
    match={")":"(","}":"{","]":"["}
    stack=[]
    for char in string:
        if char in openingbrackets:
            stack.append(char)
        elif char in closingbrackets:
            if len(stack)==0:
                return False
            if stack[-1]==match[char]:
                stack.pop()
            else:
                return False
    return len(stack)==0

string=input()
print(balancebrackets(string))
