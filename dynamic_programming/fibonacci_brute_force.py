def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
print(fibonacci(10))  # Output: 55
#time complexity is O(n^2)