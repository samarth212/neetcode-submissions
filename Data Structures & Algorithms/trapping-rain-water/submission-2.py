class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        - find the walls

        - finding the area of the gap between walls

        - return 0 if len(height) < 3

        - if our pointers val is 0, increment

        - once we find a valid l
        - case 1: keep moving r unti we hit a wall >= l
        - case 2: never find anythgn >=l (r goes our of bounds)

        - once we find l, we store the next valid r, but keep it moving, if we fail
        default to our backup r

        - store l:r pair in hashmap
        - for each pair loop l through r and calc area

        area: sum(min - height)

          l
        0,2,0,3,1,0,1,3,2,1
                            r

        [(1, 3), (3, 7), (7, 8)]

        '''

        walls = []

        l = 0


        while l < len(height)-2:
            if height[l]<1:
                l+=1
                continue
            
            rightWall = None
            for r in range(l+1, len(height)):
                if height[r] < 1:
                    continue
                if rightWall == None:
                    rightWall = r
                if height[r] > height[rightWall]:
                    rightWall = r
                if height[r] >= height[l]:
                    rightWall = r
                    break
            
            if abs(rightWall-l) > 1:
                walls.append((l, rightWall))
            l = rightWall

        print(walls)
        
        water = 0
        for l, r in walls:
            for i in range(l+1, r):
                water += (min(height[l], height[r]) - height[i])

        return water


            
            



            
            










        