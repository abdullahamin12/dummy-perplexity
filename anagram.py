class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(t)==len(s):
           return False
        count_s={}
        count_t={}
        for leter in s:
            count_s[leter]=count_s.get(leter,0)+1
        for leter in t:
            count_t[leter]=count_t.get(leter,0)+1
        if count_s==count_t:
            return True
        else:
            return False
s=Solution()
print(s.isAnagram("mama","mam"))