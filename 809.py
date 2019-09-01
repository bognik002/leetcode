class Solution:
    def split_letters(self, word):  # Returns word as list(tuple) - chars with number
        res = list()
        gr = list()
        for c in word:
            if c in gr:
                gr.append(c)
            else:
                if gr:
                    res.append((gr[0], len(gr)))
                    gr.clear()
                gr.append(c)
        if gr:
            res.append((gr[0], len(gr)))
        return res

    def check_stretchy(self, S, word):
        S = self.split_letters(S)
        word = self.split_letters(word)
        if len(S) == len(word):
            for i in range(len(S)):
                if S[i][0] == word[i][0]:
                    if S[i][1] > 2:
                        if S[i][1] >= word[i][1]:
                            pass
                        else:
                            return False
                    elif S[i][1] == word[i][1]:
                        pass
                    else:
                        return False
                else:
                    return False
        else:
            return False
        return True

    def expressiveWords(self, S, words):
        n = 0
        for word in words:
            if self.check_stretchy(S, word):
                n += 1
        return n


# Testbed
#"zzzzzyyyyy"
#["zzyy","zy","zyy"]
solution = Solution()
S = 'heeellooo'
words = ['hello', 'hi', 'helo']
print(solution.expressiveWords(S, words))