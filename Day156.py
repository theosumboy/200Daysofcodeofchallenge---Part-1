class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        n = len(heights)
        bricks_used = 0
        ladder_heap = []

        for i in range(n - 1):
            height_diff = heights[i + 1] - heights[i]

            if height_diff > 0:
                heapq.heappush(ladder_heap, height_diff)
                if len(ladder_heap) > ladders:
                    bricks_used += heapq.heappop(ladder_heap)
                if bricks_used > bricks:
                    return i

        return n - 1
