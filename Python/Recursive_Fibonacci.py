def recursive_fibonacci(n):
    """Return the nth number in the Fibonacci sequence using recursion."""
    # Base case
    if n <= 1:
        return n
    # Recursive case
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)