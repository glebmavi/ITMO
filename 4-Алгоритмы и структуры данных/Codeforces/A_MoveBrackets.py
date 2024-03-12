
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        balance = 0
        moves = 0
        for i in range(n):
            if s[i] == '(':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    moves += 1
                    balance = 0

        print(moves)
