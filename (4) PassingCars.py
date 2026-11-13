# Problem 4/ PassingCars

def solution(A):
    
    # Set the variables
    cars = 0
    passing_cars = 0
    
    # set a loop for all the cars in A
    for car in A:
        
        # Checks if there is a passing car and adds to the cars variable
        if car == 0:
            cars += 1
        
        else:
            passing_cars += cars
            
            # If the number of passing cars exceeds 1 billion
            if passing_cars > 1000000000:
                return -1
    
    return passing_cars