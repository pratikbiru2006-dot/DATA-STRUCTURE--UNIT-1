move_count = 0

def hanoi(n, src, aux, dst, print_moves=True):
    global move_count
    if n == 1:
        move_count += 1
        if print_moves:
            print(f"Move disk 1 from {src} to {dst}")
        return
    
    hanoi(n - 1, src, dst, aux, print_moves)
    
    move_count += 1
    if print_moves:
        print(f"Move disk {n} from {src} to {dst}")
        
    hanoi(n - 1, aux, src, dst, print_moves)

if __name__ == "__main__":
    print("--- Tower of Hanoi Trace for N=3 ---")
    move_count = 0 # reset
    hanoi(3, 'A', 'B', 'C', print_moves=True)
    
    print("\n--- Tower of Hanoi Move Count for N=4 ---")
    move_count = 0 # reset
    hanoi(4, 'A', 'B', 'C', print_moves=False)
    print(f"Total moves required for N=4: {move_count}")
    
    print("\n--- Complexity Statement ---")
    print("Time Complexity: O(2^n)")
    print("Every time a disk is added, the number of moves roughly doubles.")
    print("The exact formula for moves is (2^n) - 1.")