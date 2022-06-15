# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(string1, string2):
    # [assignment] Add your code here
    string1 = 'read'
    string2 = 'dear'
    str1 = sorted(string1)
    str2 = sorted(string2)
    
    if str1 == str2:
      return True
    else:
      return False
print(find_anagram('read','dear'))
