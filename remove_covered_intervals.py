class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        start = intervals[0][0]
        stop = intervals[0][1]
        remove_cnt = 0
        
        for i, e in enumerate(intervals):
            if i == 0:
                continue
            if start == e[0] and stop <= e[1]:
                remove_cnt += 1
                start = e[0]
                stop = e[1]
            elif start <= e[0] and e[1] <= stop:
                remove_cnt += 1
            else:
                start = e[0]
                stop = e[1]
        
        return len(intervals) - remove_cnt
