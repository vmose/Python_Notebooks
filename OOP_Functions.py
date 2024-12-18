# %%
def variable(A):
    a = 0
    while (a := a + 1) < max(A):
        print(a)

# %%
# Write a function that, given an array A of N integers, returns the smallest 
# positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
def solution(A):
    positive_integers = [x for x in A if x > 0]
    if not positive_integers:
        return 1
    positive_integers.sort()
    if positive_integers[0] > 1:
        return 1
    for i in range(len(positive_integers) - 1):
        if positive_integers[i + 1] - positive_integers[i] > 1:
            return positive_integers[i] + 1
    return positive_integers[-1] + 1

# %%
def wordplay(A, B):
    output = ''
    while A > 0 or B > 0:
        if A > B:
            if len(output) >= 2 and output[-2:] == 'aa':
                output += 'b'
                B -= 1
            else:
                output += 'a'
                A -= 1
        else:
            if len(output) >= 2 and output[-2:] == 'bb':
                output += 'a'
                A -= 1
            else:
                output += 'b'
                B -= 1
    return output

# %%
def worldplay(S):
    count = 0
    first_char = S[0]
    last_char = S[-1]
    if first_char == last_char:
        count += 1
    for i in range(1, len(S)):
        S = S[1:] + S[0]
        last_char = S[-1]
        if first_char == last_char:
            count += 1
    return count

# %%
def wordplay2(S):
    S = S + S
    count = 0
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            count += 1
    return count

# %%
def wordplay3(S):
    count = 0
    for i in range(len(S)):
        if S[i] == S[(i - 1) % len(S)]:
            count += 1
    return count

# %%
def min_operations(s):
    def is_vowel(c):
        return c in "aeiouAEIOU"
    s = list(s)
    count = 0
    for i in range(1, len(s)):
        if is_vowel(s[i - 1]) == is_vowel(s[i]):
            count += 1
            if is_vowel(s[i - 1]):
                for j in range(ord('a'), ord('z') + 1):
                    if chr(j) not in "aeiouAEIOU":
                        s[i] = chr(j)
                        break
            else:
                for j in "aeiouAEIOU":
                    if j not in s[:i] + s[i + 1:]:
                        s[i] = j
                        break
    return count, ''.join(s)

# %%
def stars(number):
    for i in range(1, number + 1):
        print(' ' * (number - i) + '*' * (2 * i - 1))

# %%
def maths(i):
    messages = {
        (True, True): 'wait',
        (False, True): 'go',
        (True, False): 'stop',
    }
    message = messages.get((i % 5 == 0, i % 3 == 0), i)
    print(message)

# %%
def Add_Two_Nums(l1, l2):
    rev_l1 = [l1[(i + 1) * -1] for i in range(len(l1))]
    rev_l2 = [l2[(i + 1) * -1] for i in range(len(l2))]
    return list(map(int, reversed(str(
        int(''.join([str(j) for j in rev_l1])) + 
        int(''.join([str(j) for j in rev_l2]))
    ))))

# %%
def longeststring(s):
    count = 0
    for i in range(len(s)):
        if s[i] not in s[i:]:
            count += 1
    return count

# %%
def palandrome(num):
    reversed_ = [list(str(num))[(i + 1) * -1] for i in range(len(list(str(num))))]
    return reversed_ == list(str(num))

# %%
def roman_num(num):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    p_num = 0
    for i in num[::-1]:
        if p_num > roman_dict[i]:
            number -= roman_dict[i]
        else:
            number += roman_dict[i]
        p_num = roman_dict[i]
    return number
