# %%
"""You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating 
order, starting with word1. If a string is longer 
than the other, append the additional letters onto 
the end of the merged string.

Return the merged string."""
def wordmerge(str1, str2):
    merged = []
    i=0

    while i< len(str1) and i <len(str2):
        merged.append(str1[i])
        merged.append(str2[i])
        i+=1

        merged.append(str1[i:])
        merged.append(str2[i:])

        return "".join(merged)
    
    
wordmerge("abc","def")

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

# %%
def findMaxTemperature(n, TemperatureChange):
    # Initialize the starting temperature and the maximum temperature
    current_temperature = 0
    max_temperature = current_temperature

    # Iterate through the temperature changes
    for change in TemperatureChange:
        # Update the current temperature
        current_temperature += change
        # Update the maximum temperature if the current is higher
        max_temperature = max(max_temperature, current_temperature)

    return max_temperature

# Example usage:
n = 5
TemperatureChange = [2, -3, 5, -1, 4]
print(findMaxTemperature(n, TemperatureChange))  # Output: 7
# %%

# You want to find the nth number in a series using the following parameters:
# • The first four numbers in the series are always set as n * 1 = 1 , n * 2 = 2 n * 3 = 3 n * 4 = 4 .
# • Subsequent numbers in the series are obtained by summing the four preceding numbers.
# Write a function findNthNumber that takes an integer n as input and returns the value of the nth number in the series.
# Constraints:
# 1 <= n <= 50

# Example 1
# Input:
# • n = 6
# Output:
# • 19
# Explanation:
# • The first four numbers in the series are always 1, 2, 3, 4. The fifth number in the series is obtained by summing the previous four numbers: 1 + 2 + 3 + 4 = 10. Similarly, the sixth number is obtained by summing the previous four numbers: 2 + 3 + 4 + 10 = 19

def findNthNumber(n):
    # The first four numbers in the series are fixed
    series = [1, 2, 3, 4]
    
    # If n is within the first four numbers, return it directly
    if n <= 4:
        return series[n - 1]
    
    # Generate the series until the nth number
    for i in range(4, n):
        # Add the last four numbers to get the next number in the series
        next_number = series[-1] + series[-2] + series[-3] + series[-4]
        series.append(next_number)
    
    return series[n - 1]

# Example usage
n = 6
print(findNthNumber(n))  # Output: 19

# %%
