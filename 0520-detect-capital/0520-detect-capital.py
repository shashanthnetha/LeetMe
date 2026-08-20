class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # if word.upper()==word:
        #     return True
        # elif word.lower()==word:
        #     return True
        # elif word.capitalize()==word:
        #     return True
        # else:
        #     return False

        return word.isupper() or word.istitle() or word.islower()
        