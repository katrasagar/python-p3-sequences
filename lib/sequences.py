#!/usr/bin/env python3

def print_fibonacci(length):
    """Print the first 'length' Fibonacci numbers."""
    a, b = 0, 1
    fibonacci_numbers = []

    for _ in range(length):
        fibonacci_numbers.append(a)

        
        a, b = b, a + b
    print(fibonacci_numbers)
print_fibonacci(0)
       
    
   
    
    

