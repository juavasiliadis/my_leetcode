class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center = 0
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            center = edges[0][0]
        else:
            center = edges[0][1]
        return center