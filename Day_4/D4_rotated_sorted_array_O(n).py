# Searching element in sorted and rotating array in O(n) time complexity
#brute force approach

#l = low and h = high ( ie. arr[1,2,3] then l=0 , h=2)
# key is the element to be found

def search_rotate(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
        
    return -1

arr = [5,6,7,8,9,1,2,3,4]
key = 0

i= search_rotate(arr, key)

if i != -1:
    print(f"found at index {i}")

else:
    print("not found")

