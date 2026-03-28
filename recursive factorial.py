def factorial(n):
    if n < 0: return "Invalid input"
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)

n = 4
print(f"Factorial of {n} is {factorial(n)}")
# Call Stack Trace for 4: f(4) -> 4*f(3) -> 3*f(2) -> 2*f(1) -> returns 1