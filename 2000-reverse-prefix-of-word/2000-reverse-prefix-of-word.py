class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        a=word.index(ch)
        return word[:a+1][::-1]+word[a+1:]
        