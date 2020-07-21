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
