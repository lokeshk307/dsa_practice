# My Solution
# Time Took - 36ms
# Complexity - O(N)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        final_word = ""
        for i in range(max_len):
            if i < len(word1):
                final_word += word1[i]
            if i < len(word2):
                final_word += word2[i]
        return final_word
    