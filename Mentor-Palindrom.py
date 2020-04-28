def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  

s = "kajak"
odp = isPalindrome(s) 
  
if odp: 
    print("Tak") 
else: 
    print("Nie") 