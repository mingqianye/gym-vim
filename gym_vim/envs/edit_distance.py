from typing import List

def arr_edit_distance(ss1: List[str], ss2: List[str]) -> int:
    return edit_distance("".join(ss1), "".join(ss2))

def edit_distance(s1: str, s2: str) -> int:
    if s1 == s2:
        return 0

    n = len(s1)
    m = len(s2)

    if n == 0 or m == 0:
        return max(n, m)

    # n+1 rows, m+1 cols
    dp = [[0 for j in range(m+2)] for i in range(n+2)] 

    for i in range(0, n+1):
        dp[i][0] = i

    for j in range(0, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if (s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    
    return dp[n][m]

