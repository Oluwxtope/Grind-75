class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            s_count = {}
            for char in s:
                if char not in s_count:
                    s_count[char] = 1
                else:
                    s_count[char] += 1
            t_count = {}
            for char in t:
                if char not in t_count:
                    t_count[char] = 1
                else:
                    t_count[char] += 1
            
            for char in s_count:
                if char not in t_count or s_count[char] != t_count[char]:
                    return False
            for char in t_count:
                if char not in s_count or s_count[char] != t_count[char]:
                    return False
            
            return True