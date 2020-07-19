#O(N log(N)) TC
#O(1) SC
def twonumbersum(arr,targetno):
    arr.sort()
    left=0
    right=len(arr)-1
    match=False
    while left<right:
        currentsum=arr[left]+arr[right]
        if currentsum==targetno:
            match=True
            return (arr[left],arr[right])
        elif currentsum<targetno:
            left+=1
        elif currentsum>targetno:
            right-=1
    return match
        
arr=list(map(int,input().split()))
targetno=int(input())
print(twonumbersum(arr,targetno))
