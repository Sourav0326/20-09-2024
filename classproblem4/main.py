def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
result = digital_root(45893)
print(result)
