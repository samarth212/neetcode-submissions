class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        times = []
        for i, pos in enumerate(position):
            times.append([pos, speed[i]])

        times.sort(reverse=True)

        for i, pair in enumerate(times):
            times[i] = (target - pair[0])/pair[1]
        
        stack = []


        for i in times:
            if not stack or i > stack[-1]:
                stack.append(i)

        return len(stack)

            






        