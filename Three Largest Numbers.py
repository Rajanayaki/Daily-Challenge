# TC O(N)
#SC O(1)
def threelargestnos(array):
    threelargest=[None,None,None]
    for num in array:
        updateLargest(threelargest,num)
    return threelargest
def updateLargest(threelargest,num):
    if threelargest[2] is None or threelargest[2]<num:
        Shiftandupdate(threelargest,num,2)
    elif threelargest[1] is None or threelargest[1]<num:
        Shiftandupdate(threelargest,num,1)
    elif threelargest[0] is None or threelargest[0]<num:
        Shiftandupdate(threelargest,num,0)

def Shiftandupdate(threelargest,num,index):
    for i in range(index+1):
        if i==index:
            threelargest[i]=num
        else:
            threelargest[i]==threelargest[i+1]

arr=list(map(int,input().split()))
print(threelargestnos(arr))
            
