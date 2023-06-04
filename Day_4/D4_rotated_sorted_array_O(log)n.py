# Searching element in sorted and rotating array in O(logn) time complexity


#l = low and h = high ( ie. arr[1,2,3] then l=0 , h=2)
# key is the element to be found
def search(arr,l,h,key):

    if l>h:
        return -1
    
    mid=  (l+h)//2
    if arr[mid] == key:
        return mid
    
    #if arr[l...mid] is sorted
    if arr[l] <= arr[mid]:
        if key>= arr[l] and key <= arr[mid]:
            return search( arr, l, mid-1, key)
        return search(arr, mid+1, h, key)
    

    #if arr[l...mid ] is not sorted, then arr[mid...r] must be sorted
    if key>=arr[mid] and key<=[h]:
        return search(arr, mid+1, h, key)
    return search(arr, l, mid-1, key)


if __name__ =='__main__':
    arr = [4, 5, 6, 7,8,0,1,2,3]
    key= 0
    i= search(arr, 0, len(arr)-1, key)
    if i != -1:
        print("Index: %d" %i)
    else:
        print("key not found")
