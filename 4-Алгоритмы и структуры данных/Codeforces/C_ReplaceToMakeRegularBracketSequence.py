def solve(s):
    d = {"(": ")", "{": "}", "[": "]", "<": ">"}
    reversed_d = {v: k for k, v in d.items()}
    stack = []
    count = 0

    for c in s:
        if c in d:
            stack.append(c)
        elif c in reversed_d:
            if not stack:
                return "Impossible"
            elif reversed_d[c] == stack[-1]:
                stack.pop()
            else:
                count += 1
                stack.pop()

    return count if not stack else "Impossible"


if __name__ == "__main__":
    s = input()
    print(solve(s))
