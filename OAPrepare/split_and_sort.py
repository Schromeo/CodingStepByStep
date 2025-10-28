from typing import List

def count_splits(A: List[int]) -> int:
    n = len(A)
    prefixMax = [0]*n
    suffixMin = [0]*n

    m = A[0]
    for i in range(n):
        m = max(m, A[i])
        prefixMax[i] = m

    m = A[-1]
    for i in range(n-1, -1, -1):
        m = min(m, A[i])
        suffixMin[i] = m

    ans = 0
    for i in range(n-1):
        if prefixMax[i] <= suffixMin[i+1]:
            ans += 1
    return ans
