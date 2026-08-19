class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = []

        for word in words:
            count = 0

            for ch in word:
                if ch in allowed:
                    count += 1

            if count == len(word):
                a.append(word)

        return len(a)
        