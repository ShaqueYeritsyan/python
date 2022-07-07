# Given the string, check if it is a palindrome.

def is_palindrome_using_reverse(string):
    reversed_string = "".join(reversed(string))
    # print(reversed(string))   #reversed object at 0x1045a9790
    # print(reversed_string)   #aabbaa
    return string == reversed_string

print(is_palindrome_using_reverse("aabaa"))