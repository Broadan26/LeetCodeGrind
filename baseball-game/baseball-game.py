class Solution:
    def calPoints(self, ops: list[str]) -> int:
        record = []
        for op in ops:
            if op == '+': # Add last two together
                record.append(record[-1] + record[-2])
            elif op == 'D': # Multiply last by 2
                record.append(record[-1] * 2)
            elif op == 'C': # Remove last item of list
                record.pop()
            else: # Add digits
                record.append(int(op))
        return sum(record)