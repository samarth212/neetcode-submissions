class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''

        [2,4,-6,-1]
        [-6]

        keep track of stack for pos
        when we encounter a negative asteroiud:
        add = true
            while stack and top of stack is <= new:
               
                if equal, pop from stack, add = false, break 
                if greater, pop from stack

            if add, add a to stack
        return stack
              

        '''

        stack = []

        for a in asteroids:
            add = True
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] == -a:
                        stack.pop()
                        add = False
                        break
                    elif -a > stack[-1]:
                        stack.pop()
                    else:
                        add = False
                        break
                
                if add:
                    stack.append(a)
            
        return stack

        