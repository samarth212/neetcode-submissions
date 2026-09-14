class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:

        # for every point in points, if its abs difference between x and y are same
            # calculate other points and check if exist in map
            # num of ways to make squares would be the product of all counts of the 4 points
            # increment res by ways

        
        res = 0
        x1, y1 = point

        for x2, y2 in self.points:
            ways = 0
            diffX = x1 - x2
            diffY = y1 - y2
            if x2 == x1 and y2 == y1: continue

            if abs(diffX) == abs(diffY):
                x3, y3 = x1-diffX, y1
                x4, y4 = x1, y1-diffY

                if tuple([x3, y3]) in self.points and tuple([x4, y4]) in self.points:
                    ways = self.points[tuple([x2, y2])] * self.points[tuple([x3, y3])] * self.points[tuple([x4, y4])]
                    res += ways
        
        return res
                



            


    
        
