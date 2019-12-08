#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

def is_increasing(s):
    return s[0] <= s[1] and s[1] <= s[2] and s[2] <= s[3] and s[3] <= s[4] and s[4] <= s[5]

def has_double(s):
    return s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or s[3] == s[4] or s[4] == s[5]

def has_single_pair(s):
    if s[0] == s[1] != s[2]: return True
    elif s[0] != s[1] == s[2] != s[3]: return True
    elif s[1] != s[2] == s[3] != s[4]: return True
    elif s[2] != s[3] == s[4] != s[5]: return True
    elif s[3] != s[4] == s[5]: return True
    else: return False

def main():
    puzzle_input = '156218-652527'

    count = 0
    second_count = 0
    for i in range(156218, 652527):
        s = str(i)
        if is_increasing(s) and has_double(s):
            count += 1
            if has_single_pair(s):
                second_count += 1

    print('number of possible passwords:', count)
    print('second count:', second_count)

if __name__ == "__main__":
    main()
