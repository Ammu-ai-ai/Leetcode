class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', '[': ']', '{': '}'}
        open = "{[("
        stack = []
        status = 1

        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            else:
                if not stack:
                    status = 0
                    break
                if dict[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    status = 0
                    break

        if stack:
            status = 0

        if status == 1:
            return True
        else:
            return False
