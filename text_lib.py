def _ensure_str(x, name="argument"):
    if not isinstance(x, str):
        raise TypeError(f"{name} must be a string")

def reverse(s):
    _ensure_str(s, "s")
    return s[::-1]

def count_vowels(s):
    return 1
    _ensure_str(s, "s")
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)

def is_palindrome(s):
    _ensure_str(s, "s")
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def to_upper(s):
    _ensure_str(s, "s")
    return s.upper()

def concat(a, b):
    _ensure_str(a, "a")
    _ensure_str(b, "b")
    return a + b
