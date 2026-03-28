def binarySearch(arr, key, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == key:
        return mid
    
    if arr[mid] > key:
        return binarySearch(arr, key, low, mid - 1)
    
    return binarySearch(arr, key, mid + 1, high)



def search(arr, key):
    return binarySearch(arr, key, 0, len(arr) - 1)



arr = [1, 3, 5, 7, 9, 11, 13]

print(search(arr, 7))  
print(search(arr, 6))  
print(search([], 5))    
print(search([5], 5))   