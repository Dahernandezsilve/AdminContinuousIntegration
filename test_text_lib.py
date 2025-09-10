from text_lib import reverse, count_vowels, is_palindrome, to_upper, concat
import pytest

def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("A") == "A"
    assert reverse("12345") == "54321"
    assert reverse("") == ""

def test_reverse_errors():
    with pytest.raises(TypeError): reverse(None)
    with pytest.raises(TypeError): reverse(123)

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("HELLO") == 2
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0
    assert count_vowels("aeiouAEIOU") == 10
    assert count_vowels("The quick brown fox") == 5

def test_count_vowels_errors():
    with pytest.raises(TypeError): count_vowels(123)
    with pytest.raises(TypeError): count_vowels(None)

def test_is_palindrome_ok():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("") is True

def test_is_palindrome_errors():
    with pytest.raises(TypeError): is_palindrome(123)
    with pytest.raises(TypeError): is_palindrome(None)

def test_to_upper():
    assert to_upper("hello") == "HELLO"
    assert to_upper("Hello World") == "HELLO WORLD"
    assert to_upper("") == ""
    assert to_upper("123abc") == "123ABC"

def test_to_upper_errors():
    with pytest.raises(TypeError): to_upper(123)
    with pytest.raises(TypeError): to_upper(None)

def test_concat():
    assert concat("hello", "world") == "helloworld"
    assert concat("", "world") == "world"
    assert concat("hello", "") == "hello"
    assert concat("", "") == ""
    assert concat("123", "456") == "123456"
    assert concat("mañana", " fría") == "mañana fría"

def test_concat_errors():
    with pytest.raises(TypeError): concat("hello", 5)
    with pytest.raises(TypeError): concat(None, "world")
