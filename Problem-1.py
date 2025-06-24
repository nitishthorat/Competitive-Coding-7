'''
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        heap = []

        for interval in intervals:
            if len(heap) and interval[0] >= heap[0]:
                    heapq.heappop(heap)
                    
            heapq.heappush(heap, interval[1])

        return len(heap)