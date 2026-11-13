# Problem 3/ FrogRiverOne

def solution(X,A):
    
    # set the variables
    positions = set()
    time = 0
    
    # Add the position into the set
    for position in A:
        positions.add(position)
        
        # check if the length of the position matches
        if len(positions) == X:
            return time
        
        # update the time variable
        time += 1
        
    return -1
