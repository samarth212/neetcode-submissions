class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        best = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1] :
                index, height = stack.pop()
                best = max(best, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            best = max(best, h * (len(heights) - i))

        return best
        