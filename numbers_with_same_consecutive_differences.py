from collections import deque

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        stack = deque([])
        visited = []
        num = [0] * N
        answers = []


        stack.extend([[9,1],[8,1],[7,1],[6,1],[5,1],[4,1],[3,1],[2,1],[1,1]])
        if N == 1:
            stack.append([0, 1])
        while stack:
            tmp = stack.pop()
            visited.append(tmp)
            num[tmp[1]-1] = tmp[0] * pow(10, (N-tmp[1]))
            if tmp[1] == N:
                answers.append(sum(num))
                continue
            if (tmp[0]+K) <= 9:
                if [tmp[0]+K, tmp[1]+1] not in visited or [tmp[0]+K, tmp[1]+1] not in stack:
                    stack.append([tmp[0]+K, tmp[1]+1])
            if (tmp[0]-K) >= 0 and K != 0:
                if [tmp[0]-K, tmp[1]+1] not in visited or [tmp[0]-K, tmp[1]+1] not in stack:
                    stack.append([tmp[0]-K, tmp[1]+1])
        
        return answers
