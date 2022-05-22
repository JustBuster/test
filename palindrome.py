# class Solution(object):
#     def isPalindrome(self, s):
#         s1 = ""
#         for i in s:
#             if i.isalpha:
#                 s1 += i
#         if s1 == s1[::-1]:
#             return True
        
st = "akdsjf1 32, sadf .  . ? asd"
s = ""
for i in st:
    if i.isalpha():
        s += i
        print(s)

print(s[::-1])