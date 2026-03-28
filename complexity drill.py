def single_loop(n):
    ops = 0
    for i in range(n):
        ops += 1
    print(f"Single Loop (n={n}): {ops} operations. Label: O(n)")
    print("Justification: Loops exactly 'n' times, linear scaling.\n")

def nested_loop(n):
    ops = 0
    for i in range(n):
        for j in range(n):
            ops += 1
    print(f"Nested Loop (n={n}): {ops} operations. Label: O(n^2)")
    print("Justification: Outer loop runs 'n' times, inner runs 'n' times for each outer loop (n*n).\n")

def triangular_loop(n):
    ops = 0
    for i in range(n):
        for j in range(i + 1):
            ops += 1
    print(f"Triangular Loop (n={n}): {ops} operations. Label: O(n^2)")
    print("Justification: Arithmetic progression sum n(n+1)/2. Drops constants to become O(n^2).\n")

def halving_loop(n):
    ops = 0
    current = n
    while current > 0:
        ops += 1
        current //= 2
    print(f"Halving Loop (n={n}): {ops} operations. Label: O(log n)")
    print("Justification: Input space is halved each step, scaling logarithmically.\n")

def print_search_complexities():
    print("--- Search Algorithms Reasoning ---")
    print("Linear Search:")
    print("- Best: O(1) (Target is first element)")
    print("- Avg: O(n) (Target is in the middle on average)")
    print("- Worst: O(n) (Target is last element or not present)\n")
    
    print("Binary Search:")
    print("- Best: O(1) (Target is the exact middle element)")
    print("- Avg: O(log n) (Halves search space each time)")
    print("- Worst: O(log n) (Target is at the leaf of the search tree or not present)")

if __name__ == "__main__":
    n = 10
    single_loop(n)
    nested_loop(n)
    triangular_loop(n)
    halving_loop(n)
    print_search_complexities()