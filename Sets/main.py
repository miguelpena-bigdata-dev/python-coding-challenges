# n = int(input())
# s = set(map(int, input().split()))
# for _ in range(int(input())):
#     commands = input().split()
#     match commands[0]:
#         case 'pop':
#             s.pop()
#         case 'remove':
#             s.remove(int(commands[1]))
#         case 'discard':
#             s.discard(int(commands[1]))
    
# print(sum(s))

# in_txt = 'aaabbbeeddd'
# letters = set(in_txt)

# for letter in letters:
#     print(letter)
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    letters = set(s)
    counts = {}
    for letter in letters:
        count = s.count(letter)
        counts[letter] = count
    # print(sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True))
    sorted_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: (item[1], item[0]))}
    # print(sorted_counts)
    current = 0                                         
    for k, v in sorted_counts.items():
        if current >= 3:
            break
        print(k + ' ' + str(v))
        current += 1