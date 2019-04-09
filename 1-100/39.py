# -*-coding:utf-8-*-


class Solution:
    def combinationSum(self, candidates, target):
        if len(candidates) == 0:
            return None
        self.target, self.candidates, self.res = target, candidates, []
        self.back([])
        return self.res

    def back(self, cur_seq):
        if sum(cur_seq) == self.target:
            self.res.append(cur_seq)
            return
        if sum(cur_seq) > self.target:
            return
        for num in self.candidates:
            self.back(cur_seq + [num])




s = Solution()
a = s.combinationSum([1, 3, 4, 6, 7], 7)
print(a)
