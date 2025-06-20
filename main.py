'''
#Given a list of integers, return how many of them contain an even number of digits.
def count_even_digit_numbers(nums):
    c = 0
    for num in nums:
        num_str = str(num)
        if len(num_str) % 2 == 0:
            c += 1

    return c

print(count_even_digit_numbers([12, 345, 2, 6, 7896]))  # Expected: 2
print(count_even_digit_numbers([555, 901, 482, 1771]))  # Expected: 1
'''

'''
#Given a string s containing words separated by spaces, return a new string where each word is reversed in place, but the order of words stays the same.
def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

print(reverse_words("hello world"))       # Expected: "olleh dlrow"
print(reverse_words("python is fun"))     # Expected: "nohtyp si nuf"
'''

'''
#Given a list of integers, return a new list with duplicates removed, but keep the original order of elements.
def remove_duplicates(lst):
    seen = set()
    result = []

    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([5, 1, 5, 2, 1]))
'''

'''
#Given an integer n, return a list of strings with the numbers from 1 to n with the following rules:
#-For multiples of 3, add "Fizz" instead of the number.
#-For multiples of 5, add "Buzz" instead of the number.
#-For numbers which are multiples of both 3 and 5, add "FizzBuzz".
def fizz_buzz(n):
    c = 1
    result = []
    while c <= n:
        if c % 3 ==0 and c % 5 == 0:
            result.append("FizzBuzz")
        elif c % 3 == 0:
            result.append("Fizz")
        elif c % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(c))
        c += 1
    return result

print(fizz_buzz(5)) # ["1", "2", "Fizz", "4", "Buzz"]
print(fizz_buzz(15)) # ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
'''

'''
#Given a list of test scores (0–100), return a list of grade labels based on the following:
#"A" for 90 and above
#"B" for 80–89
#"C" for 70–79
#"D" for 60–69
#"F" for below 60
def assign_grades(scores):
    result = []
    for score in scores:
        if score >= 90:
            result.append("A")
        elif score >= 80:
            result.append("B")
        elif score >= 70:
            result.append("C")
        elif score >= 60:
            result.append("D")
        else:
            result.append("F")
    return result

print(assign_grades([95, 82, 67, 59])) # ["A", "B", "D", "F"]
print(assign_grades([100, 85, 73, 60, 42])) # ["A", "B", "C", "D", "F"]
'''

'''
#Given two strings s and t, return True if they are isomorphic, otherwise return False.
#Two strings are isomorphic if the characters in s can be replaced to get t, with the following rules:
#Each character in s must map to only one character in t.
#No two characters in s can map to the same character in t.
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]

        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2

        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else: 
            t_to_s[c2] = c1
    return True


print(is_isomorphic("egg", "add")) # True  
print(is_isomorphic("foo", "bar")) # False  
print(is_isomorphic("paper", "title")) # True  
print(is_isomorphic("badc", "baba")) # False
'''

'''
#Given a string s, return the index of the first non-repeating character in the string. If there’s no unique character, return -1.
def first_unique_char(s):
    seen_char = {}
    for i in s:
        if i in seen_char:
            seen_char[i] += 1
        else:
            seen_char[i] = 1

    for i in range(len(s)):
        if seen_char[s[i]] == 1:
            return i
    return -1
            


print(first_unique_char("leetcode")) #       0, 'l' is unique, at index 0  
print(first_unique_char("loveleetcode")) #   2, 'v' is the first unique, at index 2  
print(first_unique_char("aabbcc")) #        -1, no unique characters  
'''

'''
#Given two strings s and t, return True if t is an anagram of s, and False otherwise.
#Definition:
#An anagram is a word formed by rearranging the letters of another, using all original letters exactly once.
def is_anagram(s, t):
    freq_s = {}
    freq_t = {}
    for char in s:
        if char in freq_s:
            freq_s[char] += 1
        else:
            freq_s[char] = 1
    for char in t:
        if char in freq_t:
            freq_t[char] += 1
        else:
            freq_t[char] = 1
    return freq_t == freq_s


print(is_anagram("anagram", "nagaram")) #True
print(is_anagram("rat", "car")) #False
print(is_anagram("listen", "silent")) #True
print(is_anagram("aacc", "ccac")) #False
'''

'''
#Return True if the ransom_note can be constructed using the characters in magazine.
#Each letter in magazine can only be used once.

def can_construct(ransom_note, magazine):
    ch_count = {}

    for ch in magazine:
        if ch in ch_count:
            ch_count[ch] += 1
        else:
            ch_count[ch] = 1
    
    for ch in ransom_note:
        if ch not in ch_count or ch_count[ch] == 0:
            return False
        ch_count[ch] -= 1
    return True




print(can_construct("a", "b")) # False  
print(can_construct("aa", "ab")) # False  
print(can_construct("aa", "aab")) # True  
'''