def sequential_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return f"Search element {target} found at index {i}"
    return f"Search element {target} not found in the array"
arr=[1,3,5,8,10,23,35]
print("Element:",arr)
target=10
print(sequential_search(arr,target))