#Chocolate distribution Problem
""" Given an array of N integers where each value represents the number of
chocolates in a packet. Each packet can have a variable number of chocolates.
There are m students, the task is to distribute chocolate packets such that: 
1. Each student gets one packet.
2. The difference between the number of chocolates in the packet with 
maximum chocolates and the packet with minimum chocolates given to the 
students is minimum. """

#N is number of chocolates
# m is number of students

#define function to sort array

def findmindiff(arr, n, m):

    #return 0 if no chocolates or no students
    if (m == 0 or n == 0):
        return 0
    
    # sort array
    arr.sort()


    #no of students can't be greater than chocolates
    if(n<m):
        return -1
    
    #find min difference or initialise first min_diff value
    min_diff = arr[n-1] - arr[0]

    #run the loop n-m+1 times
    for i in range(len(arr)-m+1):

        #calculating new difference and comparing the 
        # minimum among previous and the latest
        min_diff = min( min_diff , arr[i+m-1] - arr[i])

        return min_diff

if __name__ == "__main__": 
    arr = [12, 4, 7, 9, 2, 23, 25, 41,30, 40, 28, 42, 30, 44, 48, 43, 50]
    m= 7
    n= len(arr)

    print("minimum difference is ", findmindiff(arr,n,m))

