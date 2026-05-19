class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
     Dict= {};

     for word in strs:
        word_sort="".join(sorted(word))

        if word_sort in Dict:
            Dict[word_sort].append(word)

        else:
           Dict[word_sort]=[word]

     return list(Dict.values())

