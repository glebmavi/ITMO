def solve(lines):
    scores = {"": float("-inf")}
    round_scores = []
    max_player = ""
    for l in lines:
        i = l.split()
        if i[0] in scores:
            scores[i[0]] += int(i[1])
        else:
            scores[i[0]] = int(i[1])
        round_scores.append((i[0], scores[i[0]]))

    max_score = max(scores.values())
    for player, score in round_scores:
        if score >= max_score and scores[player] == max_score:
            max_player = player
            break

    print(max_player)


if __name__ == "__main__":
    n = int(input())
    lines = []
    for i in range(n):
        s = input()
        lines.append(s)
    solve(lines)
