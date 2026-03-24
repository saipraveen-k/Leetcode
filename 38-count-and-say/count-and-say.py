class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for _ in range(n - 1):
            result = self.getNext(result)
        return result
    
    def getNext(self, s):
        i = 0
        next_str = ""
        while i < len(s):
            char = s[i]
            count = 1
            while i + count < len(s) and s[i + count] == char:
                count += 1
            next_str += str(count) + char
            i += count
        return next_str