import sys
input = sys.stdin.readline
from collections import Counter

def min_removals_to_make_peragram():
    s = input().strip()
    
    freq = Counter(s)
    
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    print(max(0, odd_count - 1))

min_removals_to_make_peragram()
