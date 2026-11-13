# Problem 5/ MissingInteger

def solution(A):
    
    # Set the variables
    num = set(A)
    smallest = 1
    
    # Set a loop to check for the smallest number in the set
    while smallest in num:
        smallest += 1
        
    # Returns the smallest number
    return smallest