"""
https://codeforces.com/contest/1101/problem/B
"""

accord = input()

open_bracket = accord.find("[")
accord=accord[open_bracket+1:]
open_colon = accord.find(":")
accord = accord[open_colon+1:]
close_bracket = accord.rfind("]")
close_colon = accord[:close_bracket].rfind(":")

if open_bracket == -1 or open_colon == -1 or close_bracket == -1 or close_colon == -1:
    print(-1)
else:
    res = accord[:close_colon].count("|")+4
    print(res)
