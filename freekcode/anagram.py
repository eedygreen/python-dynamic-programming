class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """©freekcode
        check the length of the two strings return false if they are not equal
        count the occurence of each character in the string using key value pair
            variable: hash table
            parameter: string

        compare the two dictionaries
        """

        if len(s) != len(t):
            return False
        
        hash_s, hash_t = {}, {}
        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0) # get the value of the key, if not found, return 0
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        return hash_s == hash_t

        # NOTE: the following code is also working

        if sorted(s) == sorted(t):
            return True

        return Counter(s) == Counter(t)
        