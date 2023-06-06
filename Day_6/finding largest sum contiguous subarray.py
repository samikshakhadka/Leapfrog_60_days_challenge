# finding largest sum contiguous subarray
#Kadane's algorithm

# sys is a module
from sys import maxsize 

def maxsubarraysum(a, size):

    max_so_far = -maxsize-1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0 # keep track of starting index of current subarray

    for i in range(0,size):

        max_ending_here += a[i] # keep track of max sum ending at current position in array.

        if max_so_far<max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here<0:
            max_ending_here=0
            s= i+1

        print("Maximum contiguous sum is %d" %(max_so_far))
        print("starting index %d" %(start))
        print("ending index %d" %(end))


a= [1,2-3,4,5,-8,3,4]
maxsubarraysum(a, len(a))


