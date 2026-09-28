class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = 0
        records = []

        for op in operations:
            if op == '+':
                if len(records) == 1:
                    res += records[-1]
                elif len(records) > 1:
                    res += records[-1] + records[-2]

                records.append(records[-1] + records[-2])
            elif op == 'D':
                res += records[-1]*2
                records.append(records[-1]*2)
            elif op == 'C':
                res -= records.pop()
            else:
                records.append(int(op))
                res+=int(op)
        
        return res

        