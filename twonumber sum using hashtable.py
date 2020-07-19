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
