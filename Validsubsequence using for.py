#using for
def validsubseq(arr,seq):
    subind=0
    for i in arr:
        if subind==len(seq):
            break
        if i==seq[subind]:
            subind+=1        
    return subind==len(seq)
arr=list(map(int,input().split()))
seq=list(map(int,input().split()))
print(validsubseq(arr,seq))

#using while
def validsubsequence(arr,seq):
    arrind=0
    subind=0
    while arrind<len(arr) and subind<len(seq):
        if arr[arrind]==seq[subind]:
            subind+=1
        arrind+=1
    return subind==len(seq)

arr=list(map(int,input().split()))
seq=list(map(int,input().split()))
print(validsubsequence(arr,seq))
