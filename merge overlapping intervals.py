def mergeoverlapping(arr):
    arr.sort(key=lambda x:x[0])
    stack=[arr[0]]
    for i in range(1,len(arr)):
        top=stack[-1]
        if top[1] < arr[i][0]:
            stack.append(arr[i])
        elif top[1] < arr[i][1]:
            top[1]=arr[i][1]
            stack.pop()
            stack.append(top)
    return stack

arr=[[1,3],[2,4],[5,7],[6,8]]
merged=mergeoverlapping(arr)
for m in merged:
    print(m,end=" ")
            
