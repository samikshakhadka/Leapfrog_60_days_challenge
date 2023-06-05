#find missing element in sorted array
#using mathematical concept
# fist find the total(actual)  sum of that limit and
#find the current sum of the array
#then sub (actual sum - current sum)
# the difference is the missing number

class A:

    @staticmethod
    def getmissingno(a,n):

        total_sum = int(((n+1)*(n+2))/2)

        #initialise sum
        sum= 0
        i=0
        while(i<n):
            sum += a[i]
            i += 1
        return total_sum - sum
    
    @staticmethod
    def main(args):
        a= [1,2,3,5,6,7]
        n= len(a)
        print(A.getmissingno(a,n), end= "")


if __name__ == "__main__":
    A.main([])
