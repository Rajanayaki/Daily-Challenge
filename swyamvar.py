size=int(input())
bride=list(input())
groom=list(input())
count=0
i=0
j=0
while i<len(bride) and j<len(groom):
        if groom[0]==bride[i]:
            groom.remove(groom[0])
            bride.remove(bride[i])
            matched=True
            j=0
            count+=1
        else:
             g=groom.pop(0)
             groom.append(g)
             j+=1
             matched=False
        if matched==False and j==len(groom):
            break 

print(size-count)
