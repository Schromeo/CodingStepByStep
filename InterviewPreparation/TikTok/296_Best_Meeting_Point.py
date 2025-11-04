from typing import List


class Solution:
    def minTotalDistance(self, G: List[List[int]]) -> int:
        nR,nC = len(G),len(G[0])
        
        LR = [ sum(row) for row in G ]
        LC = [ sum(row) for row in list(zip(*G)) ]
        n1 = sum(LR)

        retV = 0
        # print (LR, LC)
        for L in (LR, LC):

            sm = sum( i*c for i,c in enumerate(L) )
            cnt = n1
            # print (cnt)
            for i,c in enumerate(L):
                cnt -= 2*c
                if cnt<0:      break
                sm -= cnt
                # print (cnt, sm)
            retV += sm

        return retV
        
        