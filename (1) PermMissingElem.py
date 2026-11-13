# Problem 1/ PermMissingElem

def solution(A):
    
    # Set the variables
    n = set(A)
    missing = 1
    
    # Set a loop to go through all the numbers in the set
    while missing in n:
        missing += 1
        
    return missing