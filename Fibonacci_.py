class FibonacciExplorer:
    def __init__(self):
        self.naive_calls = 0
        self.memo_calls = 0
        self.memo_cache = {}

    def fib_naive(self, n):
        self.naive_calls += 1
        if n <= 1:
            return n
        return self.fib_naive(n - 1) + self.fib_naive(n - 2)

    def fib_memo(self, n):
        self.memo_calls += 1
        # Check if already calculated
        if n in self.memo_cache:
            return self.memo_cache[n]
        
        # Base cases
        if n <= 1:
            return n
            
        # Recursive step with storage
        self.memo_cache[n] = self.fib_memo(n - 1) + self.fib_memo(n - 2)
        return self.memo_cache[n]

    def reset_counts(self):
        self.naive_calls = 0
        self.memo_calls = 0
        self.memo_cache = {}


explorer = FibonacciExplorer()
test_values = [10, 20, 25] 

print(f"{'n':<5} | {'Result':<10} | {'Naive Calls':<15} | {'Memo Calls':<15}")
print("-" * 55)

for n in test_values:
    explorer.reset_counts()
    res = explorer.fib_memo(n)
    explorer.fib_naive(n) 
    print(f"{n:<5} | {res:<10} | {explorer.naive_calls:<15} | {explorer.memo_calls:<15}")