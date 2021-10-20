class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        second = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        third = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        answer = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(first) or word_set.issubset(second) or word_set.issubset(third):
                answer.append(word)
        return answer