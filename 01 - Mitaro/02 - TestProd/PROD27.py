import sys

def find_max_cashback():
    input = sys.stdin.read
    data = input().splitlines()
    M, N = map(int, data[0].split())
    kolya_cashbacks = [tuple(map(int, line.split())) for line in data[1:M + 1]]
    borya_cashbacks = [tuple(map(int, line.split())) for line in data[M + 1:M + 1 + N]]
    kolya_max_month = max(kolya_cashbacks, key=lambda x: x[1])[0] if kolya_cashbacks else 0
    borya_max_month = max(borya_cashbacks, key=lambda x: x[1])[0] if borya_cashbacks else 0
    print(kolya_max_month, borya_max_month)

if __name__ == "__main__":
    find_max_cashback()
