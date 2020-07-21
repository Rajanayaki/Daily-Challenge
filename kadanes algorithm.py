def kadanes_algorithm(arr):
    curr_max=arr[0]
    max_so_far=arr[0]
    for i in range(len(arr)):
        curr_max=max(arr[i],curr_max+arr[i])
        max_so_far=max(curr_max,max_so_far)
    return max_so_far

arr=list(map(int,input().split()))
print(kadanes_algorithm(arr))
