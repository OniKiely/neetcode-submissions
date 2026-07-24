class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                arr.append(char)
            if char == ")":
                if not arr or arr.pop() != "(":
                    return False
            if char == "}":
                if not arr or arr.pop() != "{":
                    return False
            if char == "]":
                if not arr or arr.pop() != "[":
                    return False
        
        # check if all Parentheses have been closed
        if arr:
            return False

        return True

            
        