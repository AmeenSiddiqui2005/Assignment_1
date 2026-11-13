# Problem 2/ PermCheck

def solution(A):
    
    # set the length of the array
    n = len(A)
    
    # Check the length of the set and the max of the set
    if len(set(A)) == n and max(A) == n:
        
        # Returns 1 if the conditions are met
        return 1
    
    # Returns 0 if the conditions are not met
    return 0