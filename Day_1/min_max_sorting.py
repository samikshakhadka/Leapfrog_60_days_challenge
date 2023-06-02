def getMinMax(arr):
    arr.sort()
    minmax = { "min":arr[0], "max": arr[-1]}
    return minmax

arr= [1, 0, 100, 200, 50, 79, 80]
minmax= getMinMax(arr)

print("minimum element is ", minmax['min'])
print("maximum element is ", minmax["max"])

