class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sInArr = s.split(" ")   
        s = ""
        for i in range(1, len(sInArr) + 1):
            for word in sInArr:
                if int(word[len(word) - 1]) == i:
                    s += word[:len(word) - 1]
                    if i != len(sInArr):
                        s += " "
                    break
            
        return s