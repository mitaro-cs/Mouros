import sys

def process_transactions():
    input = sys.stdin.read
    data = input().splitlines()
    N, M = map(int, data[0].split())
    balances = {}
    for i in range(1, N + 1):
        ID, S = map(int, data[i].split())
        balances[ID] = S

    for i in range(N + 1, N + 1 + M):
        A, B, X = map(int, data[i].split())
        if balances[A] >= X:
            balances[A] -= X
            balances[B] += X

    for ID in sorted(balances):
        print(ID, balances[ID])

if __name__ == "__main__":
    process_transactions()
