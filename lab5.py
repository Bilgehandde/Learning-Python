# -*- coding: utf-8 -*-
"""
OLCHLT

"""
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"


def problem1(inp, n):
   
    counts = {}
    for num in inp:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    result = [num for num in counts.keys() if counts[num] == n]

    return result

def problem2(class_grades):
    if not class_grades:
        return 0

    sorted_grades = sorted(class_grades, key=class_grades.get)
    num_students = len(sorted_grades)
    if num_students % 2 == 1:

        median_grade = class_grades[sorted_grades[num_students // 2]]
    else:
        middle1 = class_grades[sorted_grades[num_students // 2 - 1]]
        middle2 = class_grades[sorted_grades[num_students // 2]]
        median_grade = (middle1 + middle2) / 2
    # output type is float
    return median_grade


def problem3(ffunc, n):
    def test_false(n):
        # Count the number of 1's up to (including) the given number starting from 0
        count = 0
        for i in range(n + 1):
            count += str(i).count('1')
        
        # Simulate an incorrect result by adding 1 to the final count
        count += 1
        return count
    
    def test(n):
        return sum(str(i).count('1') for i in range(n + 1))


    def check_ffunc_correctness(ffunc, n):
        count = 0
        for i in range(n + 1):
            count += str(i).count('1')
        return count

    return ffunc(n) == check_ffunc_correctness(ffunc, n)

def problem4(s):

    s = s.lower()
    result = []
    def helper(letter, string):
        if letter and letter not in result: 
            result.append(letter)

        for i in range(len(string)):
            helper(letter + string[i], string[:i] + string[i+1:])
    helper('', s)

    return sorted(result)

def problem5(s):
    compressed = ""
    count = 1

    i = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + (str(count) if count > 1 else "")
            count = 1
        i += 1

    compressed += s[-1] + (str(count) if count > 1 else "")

    o_size = len(s)
    c_size = len(compressed)

    percentage = int(((o_size - c_size) / o_size) * 100)

    return compressed, percentage