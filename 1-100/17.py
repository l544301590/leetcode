# -*-coding:utf-8-*-


class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        alpha = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.res, self.alpha = [], []
        for d in digits:
            self.alpha.append(alpha[int(d)])
        self.helper(0, "")
        return self.res

    def helper(self, index, res):
        if index == len(self.alpha):
            self.res.append(res)
            return
        for ch in self.alpha[index]:
            self.helper(index + 1, res + ch)


s = Solution()
a = s.letterCombinations("234")
print(a)