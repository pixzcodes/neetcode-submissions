class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        list_s = list(s)
        list_t = list(t)

        for l in list_s:
            if l in list_t:
                list_t.remove(l)
        if len(list_t) == 0:
            return True
        else:
            return False
