class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        d = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in d:
                d[sortedWord] = [word]
            else:
                d[sortedWord].append(word)

        for val in d.values():
            out.append(val)
        return out
