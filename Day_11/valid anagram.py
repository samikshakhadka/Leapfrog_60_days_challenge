# valid anagram

class findanagram:

    def isanagram(self, a,b):

        if sorted(a) == sorted(b):
            return True
        else:
            return False
        

if __name__ == '__main__':
    a= "silent"
    b="listen"

    if (findanagram().isanagram(a,b)):
        print("The two string are anagram")
    else:
        print("The two strings aren't anagram")
        