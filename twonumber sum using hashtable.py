#using hashtable
#O(N) TC
#O(N) SC
def twonumbersum(arr,targetno):
    hashtable={}
    curr=0
    for i in arr:
        curr=targetno-(i)
        if curr in hashtable:
            return curr,i
        else:
            hashtable[i]=True


arr=list(map(int,input().split()))
targetno=int(input())
print(twonumbersum(arr,targetno))

#using pointers
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
