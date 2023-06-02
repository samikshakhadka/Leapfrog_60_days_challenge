# reverse an array or string

#recursive method

#initialise start =n and end = n-1
#define function to reverse list

def reverselist(A, start, end):
    if start>=end:
        return
    A[start],A[end] = A[end], A[start]
    reverselist(A, start+1, end-1)


#define list
A= ["S","A","M","I","K","S","H","A"]
print("The original string is :", A)

reverselist(A,0,7)
print("The reverse list is :", A)