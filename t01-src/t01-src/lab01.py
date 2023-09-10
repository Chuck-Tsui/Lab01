# File: lab01.py

# Replace the following by your full name and 8-digit student number
student_name = "Xu Xiaochi"
student_id = "12556828"

from random import random

def palindrome_recur(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome_recur(s[1:-1])


def myth_value(n):
    pass  # replace this line by your code

if __name__ == "__main__":
    print("Testing palindrome_recur",palindrome_recur("abba")) 
    print("Testing palindrome_recur",palindrome_recur("abeca"))
