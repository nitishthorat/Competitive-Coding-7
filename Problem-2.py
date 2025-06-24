'''
    *** Binary Search***
    Time Complexity: O(logR * nlog(n))
    Space Complexity: O(1)
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        low = matrix[0][0]
        high = matrix[n-1][n-1]

        while low < high:
            mid = low + (high - low) // 2

            total_elements = 0
            for i in range(n):
                no_elements = self.upperBound(matrix[i], mid, n)
                total_elements += no_elements

            if total_elements >= k :
                high = mid
            else:
                low = mid + 1

        return low

    def upperBound(self, row, key, n):
        low = 0
        high = n-1

        while low <= high:
            mid = low + (high-low) // 2

            if row[mid] <= key:
                low = mid + 1
            else:
                high = mid - 1

        return low

'''
    *** Heaps ***
    Time Complexity: O(n*nlog(k))
    Space Complexity: O(k)
'''   
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, -matrix[i][j])

                if len(heap) > k:
                    heapq.heappop(heap)

        return -heap[0]
