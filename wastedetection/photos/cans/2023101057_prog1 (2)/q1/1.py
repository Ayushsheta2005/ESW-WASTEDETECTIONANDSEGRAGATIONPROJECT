def prng(N, S, X, transitions):
    freq = [0] * N
    current_state = S - 1
    
    for _ in range(X):
        freq[current_state] += 1
        current_state = transitions[current_state]
    
    return freq

def main():
    T = int(input().strip())
    
    for _ in range(T):
        N, M, S, X = [int(x) for x in input().strip().split()]
        transitions = [-1] * N
        
        for _ in range(M):
            ai, bi = [int(x) for x in input().strip().split()]
            transitions[ai-1] = bi-1
        
        result = prng(N, S, X, transitions)
        
        for frequency in result:
            print(frequency, end=' ')
        print()

if __name__ == "__main__":
    main()
