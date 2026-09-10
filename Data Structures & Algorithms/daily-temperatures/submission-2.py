class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for ind, temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                prevInd = stk.pop()
                res[prevInd] = ind - prevInd
            stk.append(ind)

        return res