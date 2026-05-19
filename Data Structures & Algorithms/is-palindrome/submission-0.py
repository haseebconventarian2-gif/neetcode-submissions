class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned= ""
        for char in s:
         if char.isalnum():
            cleaned = cleaned + char.lower()

        reverse_string= ""    

        for i in range(len(cleaned)-1,-1,-1):
        

         reverse_string= reverse_string + cleaned[i]
            
        if reverse_string == cleaned:
         return True
        else:
            return False



       
        