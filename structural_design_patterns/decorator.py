import functools

def uppercase_decorator_annotation(func):
    """Decorator to convert function output to uppercase."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator_annotation
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

# Another example: Memoization decorator
def memoize(func):
    """Decorator to cache function results."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci_function(n):
    """Computes the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci_function(n-1) + fibonacci_function(n-2)

# Testing the decorators
print(greet("Alice"))
print(fibonacci_function(10))
