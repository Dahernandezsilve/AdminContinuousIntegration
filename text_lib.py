def reverse(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == reverse(cleaned)

def to_upper(s):
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    return s.upper()

def concat(a, b):
    return a + b