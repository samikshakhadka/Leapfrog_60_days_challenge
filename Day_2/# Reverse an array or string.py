# Reverse an array or string

#Iterative way

#initialise start =n and end = n-1
#define function to reverse list


def reverselist(A, start, end):
    while start <end:
        A[start],A[end] = A[end], A[start]
        start += 1
        end -= 1


A= [1, 2,3,4,5]
print("The original list is : ", A)
reverselist(A,0,4)

print("The reversed list is :", A)
