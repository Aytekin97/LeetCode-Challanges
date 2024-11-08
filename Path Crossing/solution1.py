class Solution(object):
    def isPathCrossing(self, path):
        x = 0
        y = 0
        points_list = [[x, y]]
        for i in path:
            if i == 'N':
                y += 1
            if i == 'S':
                y -= 1
            if i == 'W':
                x -= 1
            if i == 'E':
                x += 1
            point = [x, y]            
            print(point)
            if point in points_list:
                return True
            points_list.append(point)
        return False
            
obj = Solution()
print(obj.isPathCrossing("NNSWWEWSSESSWENNW"))