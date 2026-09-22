class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for c in operations:
            if c == '+':
                res = record[-2] + record[-1]
                record.append(res)
            elif c == 'D':
                res = record[-1]*2
                record.append(res)                
            elif c == 'C':
                record.pop()
            else:
                record.append(int(c))
        return sum(record)