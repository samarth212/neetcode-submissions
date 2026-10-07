class Solution:
    def simplifyPath(self, path: str) -> str:

        '''

        loop through path (while)
        - if we encounter a /, continue forward until we meet a non / char
        - if we meet any alphabetical char, 
            - build direcotry string
            - continue forward until you hit a slash or end
            - add to stack
        - if we meet a .
            - build a dir string
            - continue until slash or end
            - if the dir is == .., pop from stack
            - if dir = ., skip
            - else, add to stack

        loop through resulting stack and build result (/.join) if stakc is empty then /

        '''

        i = 0
        d = []
        stack = []

        while i < len(path):
            print(stack)
            if path[i] == '/':
                directory = ''.join(d)
                if directory == '..':
                    stack.pop() if stack else None
                elif directory != '.' and directory != '':
                    stack.append(directory)
                d = []
                i+=1
            
            else:
                d.append(path[i])
                i+=1
        
        if d:
            stack.append(''.join(d))

        if not stack:
            return '/'
        
        return '/'+'/'.join(stack)



        