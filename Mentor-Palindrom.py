def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  

s = "bumtaratarabum"
odp = isPalindrome(s) 
  
if odp == True: 
    print("Tak") 
else: 
    print("Nie") 