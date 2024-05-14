##
## =======================================================
## Paul Park (20949359)
## CS 234 Spring 2024
## Assignment 0, Problem 1
## =======================================================
##

import modules.check as check

def sum_of_three(num: int):
    """
    sum_of_three(num) -> int
    
    Adds three integers (2 given 1 provided by user) and returns the sum.

    Examples:
    sum_of_three(0) => 69
    """
    # this is the numher found in teams chat
    Consulting_OfficeHours = 27
    # this is the number found in edX
    edX = 42
    return Consulting_OfficeHours+edX+num

# Testing the add function
check.expect("Test1", sum_of_three(0), 69)
check.expect("Test2", sum_of_three(1), 70)

