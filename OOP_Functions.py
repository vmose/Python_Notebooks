
def variable(A):
    a=0
    while (a:=a+1) < max(A):
        print(a)
        
# Write a function that, given an array A of N integers, returns the smallest 
# positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

def solution(A):
    # Remove all non-positive integers
    positive_integers = [x for x in A if x > 0]
    
    # If there are no positive integers, return 1
    if not positive_integers:
        return 1
    
    # Sort the list of positive integers
    positive_integers.sort()
    
    # If the smallest positive integer is greater than 1, return 1
    if positive_integers[0] > 1:
        return 1
    
    # Find the smallest positive integer that does not occur in the sorted list
    for i in range(len(positive_integers) - 1):
        if positive_integers[i + 1] - positive_integers[i] > 1:
            return positive_integers[i] + 1
    
    # If all integers from 1 to the maximum in the list are present, return the next integer
    return positive_integers[-1] + 1
solution([1,2,4,6,2])
3
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
def solution(A):
    list = set(x for x in A if x>0)

    i=1
    while i in list:
        i+=1
    return i
# Initially, string S of length N is given. 
# Then N-1 operations are applied to it: remove the first letter of S and add it to the end. 
# How many times is the first letter of S the same as the last letter? 
# Write a python function: def solution (S) that given a 
# string S of length N consisting of letters "a" and/or "b" returns the number of times the 
# first letter is the same as the last in the obtained sequence of strings

def worldplay(S):
    # Initialize the count to 0
    count = 0
    
    # Get the first and last characters of S
    first_char = S[0]
    last_char = S[-1]
    
    # Check if the first and last characters are the same
    if first_char == last_char:
        count += 1
    
    # Compute the number of times the first letter is the same as the last
    for i in range(1, len(S)):
        # Remove the first character of S and add it to the end
        S = S[1:] + S[0]
        
        # Get the new last character of S
        last_char = S[-1]
        
        # Check if the first and last characters are the same
        if first_char == last_char:
            count += 1
    
    return count
print(worldplay('abbbabaa'))
print(worldplay('abab')) #output should be 0
4
2
def wordplay2(S):
    # Concatenate the input string with itself
    S = S + S
    count = 0
    for i in range(len(S)-1):
        # Check if the first and last characters of the current substring are the same
        if S[i] == S[i+1]:
            count += 1
    return count
print(wordplay2('abbbabaa'))#output should be 4
print(wordplay2('abab'))
7
0
def wordplay3(S):
    count = 0
    for i in range(len(S)):
        # Check if the first and last characters of the current substring are the same
        if S[i] == S[(i-1)%len(S)]:
            count += 1
    return count
def wordcount4(string):
    vowel = 'a'
    count = 0
    for i in range (1,len(string)):
        string = string[1:] + vowel
        
        char_1 = string[0]
        char_n= string[-1]
        if char_1==char_n:
            (count:=count+1)
        
        return count
#You are given a string S of size N. 
#In one operation you can replace and character of the string with any other character. 
#find the minimum number of operations required so that no two vowels or consonants are adjacent.

def min_operations(s):
    # Helper function to check if a character is a vowel
    def is_vowel(c):
        return c in "aeiouAEIOU"

    # Convert the string to a list of characters for easy manipulation
    s = list(s)

    # Initialize the count of operations to zero
    count = 0

    # Loop through the string and swap adjacent vowels or consonants
    for i in range(1, len(s)):
        if is_vowel(s[i-1]) == is_vowel(s[i]):
            # If two adjacent characters are of the same type, we need to swap one of them
            count += 1
            if is_vowel(s[i-1]):
                # If both characters are vowels, we can swap one with a consonant
                for j in range(ord('a'), ord('z')+1):
                    if chr(j) not in "aeiouAEIOU":
                        s[i] = chr(j)
                        break
            else:
                # If both characters are consonants, we can swap one with a vowel
                for j in "aeiouAEIOU":
                    if j not in s[:i] + s[i+1:]:
                        s[i] = j
                        break

    # Convert the list back to a string and return the count of operations
    return count, ''.join(s)
min_operations("ttt")
(1, 'tat')
def stars(number):
    for i in range(1, number+1):
        print(' ' * (number - i) + '*' * (2 * i - 1))
stars(5)
    *
   ***
  *****
 *******
*********
def maths(i):
    if i%5==0 and i%3==0:
        print('wait')
    elif i%5==0:
        print('stop')
    elif i%3==0:
        print('go')
    else:
        print(i)
maths(8)
8
def maths(i):
    messages = {
        (True, True): 'wait',
        (False, True): 'go',
        (True, False): 'stop',
    }
    message = messages.get((i % 5 == 0, i % 3 == 0), i)
    print(message)
maths(7)
7
def Add_Two_Nums(l1,l2):
    rev_l1 = []
    rev_l2 = []
    for i in range(len(l1)):
        rev_l1.append(l1[(i+1)*-1])
    for i in range(len(l2)):
        rev_l2.append(l2[(i+1)*-1])
    return list(map(int, reversed(str(int(''.join([str(j) for j in rev_l1])) + int(''.join([str(j) for j in rev_l2]))))))
Add_Two_Nums([0,0,5],[0,0,5])
[0, 0, 0, 1]
def longeststring(s):
    count = 0
    for i in range(len(s)):
        if s[i] not in s[i:]:
            (count:=count+1)
    return count
longeststring('qwertyuiop')
0
list(str(num))
['2', '0', '0', '1']
def palandrome(num):
    reversed_ = []
    for i in range(len(list(str(num)))):
        reversed_.append(list(str(num))[(i+1)*-1])
    return reversed_ == list(str(num))
palandrome(5005)
True
dict = {'I':1,'V':5,'X':10,'C':100,'D':500,'M':1000}
def roman_num(num):
    dict = {'I':1,'V':5,'X':10,'C':100,'D':500,'M':1000}
    number = 0
    p_num = 0
    for i in num[::-1]:
        if p_num>dict[i]:
            (number:=number-dict[i])
        else:
            (number:=number+dict[i])
        p_num = dict[i]
    return number  
roman_num('XX')
20
list(map(int, reversed(str(456))))
[6, 5, 4]
 
