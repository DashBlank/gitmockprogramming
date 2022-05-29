def climbingLeaderboard(ranked, player):
    results = []
    ranked = list(sorted(set(ranked), reverse=True))
    current_rank = len(ranked) - 1
    for score in player:
        if current_rank == -1:
            results.append(1)
        else:
            while current_rank > -1 and score >= ranked[current_rank]:
                current_rank -= 1
            results.append(current_rank + 2)

    for result in results:
        print(result)


ranked_count = int(input())
ranked = list(map(int, input().split()))

player_count = int(input())
player = list(map(int, input().split()))

climbingLeaderboard(ranked, player)
