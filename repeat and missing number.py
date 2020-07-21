def find_num(arr):
    for i in range(0,len(arr)):
        if arr[abs(arr[i])-1]>=0:
            arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        else:
            print(abs(arr[i]),end=" ")
    for i in range(0,len(arr)):
        if arr[i]>0:
            print(i+1,end=" ")
arr=list(map(int,input().split()))
find_num(arr)
