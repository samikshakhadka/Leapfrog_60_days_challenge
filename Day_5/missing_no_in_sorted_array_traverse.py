#Find the missing number in a sorted array 

#traverse all elements

def getmissingno(a):

    n= len(a)

    for i in range(n):
        if(a[i] != i+1):
            return i+1
        
        return n+1
    

a= [1,2,3,5,6]
print(getmissingno(a))