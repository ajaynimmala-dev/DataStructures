class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        string_length = len(s)
        word_length = len(words[0])
        num_words = len(words)
        data = {}
        total = num_words * word_length
        for i in words:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        res = []
        for i in range(word_length):
            left = i
            right = i
            visited = 0
            curr = {}
            while right + word_length <= string_length:
                word = s[right:right + word_length]
                right += word_length
                if word in data:
                    if word in curr:
                        curr[word] += 1
                    else:
                        curr[word] = 1
                    visited += 1
                    while curr[word] > data[word]:
                        word_remove = s[left:left + word_length]
                        print(word_remove)
                        left = left + word_length
                        curr[word_remove] -= 1
                        visited -= 1
                    if visited == num_words:
                        res.append(left)
                else:
                    curr.clear()
                    left = right
                    visited = 0
        return res



