# Check if given string of brackets is balanced or not

def balanced(expr):

    stack = []

    for char in expr:
        if char in ["( ", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(" :
                if char != ")":
                    return False
            if current_char == "[" :
                if char != "]":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
                    
    if stack:
        return False
    return True
    

if __name__ == "__main__":
    expr = "{()}"


    if balanced(expr):
        print("the string is balanced")

    else:
        print("string is not balanced")


