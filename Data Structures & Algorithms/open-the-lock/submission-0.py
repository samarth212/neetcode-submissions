class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        seen = set(deadends)
        if '0000' in seen:
            return -1
        q = deque(['0000'])
        seen.add('0000')
        level = 0

        

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node == target:
                    return level
                
                for i in range(len(node)):
                    up = node[:i] + str((int(node[i])+1)%10) + node[i+1:]
                    down = node[:i] + str((int(node[i])-1)%10) + node[i+1:]

                    if up not in seen:
                        seen.add(up)
                        q.append(up)
                    if down not in seen:
                        seen.add(down)
                        q.append(down)

            level +=1

    
        return -1
