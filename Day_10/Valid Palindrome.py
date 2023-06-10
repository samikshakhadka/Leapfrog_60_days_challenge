#Valid Palindrome

def ispalindrome(s):

    #replace white space
    s1= s.replace(' ', '')

    #make them lowercase
    s1= s1.lower()

    #reverse the string
    s2 = s1[::-1]
    return True if s1==s2 else False


s= "Yo banana boy"

if(ispalindrome(s)):
    print("sentence is palindrome")

else:
    print("sentence is not palindrome")
    

