# Description: Fibonacci sequence implementation
def fibonacci_iterative(n):
    

def fibonacci_recursive(n):
    if n<0:
        return -1;

    if n<2:
        return n;

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2);

cache = {}

def fibonacci_recursive_with_memory(n):
    if n<0:
        return -1;

    if n<2:
        return n;

    if n in cache:
        return cache[n];

    cache[n] = fibonacci_recursive_with_memory(n-1) + fibonacci_recursive_with_memory(n-2);

    return cache[n];