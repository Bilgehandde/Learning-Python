# -*- coding: utf-8 -*-
"""
OLCHLT
"""
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem1(a):
    if 'K' in a:
        return True
    else :
        return False
        
def problem2(num1,num2,num3,num4):
    return float(min(num1,num2,num3,num4))

def problem3(num1,num2):
    if 0 < num1 < 1 and 0 < num2 < 1 :
        if num2 == 0.5:
            return 1
        return round(num2)
    if num1 > num2 :
        if abs(num1 - round(num1)) == 0.5 or abs(num1 - round(num1)) == 0:
            return num1
        num1 = num1 - 0.5
        return round(num1)
    if num1 < num2:
        if abs(num1 - round(num1)) == 0.5 or abs(num1 - round(num1)) == 0:
            return num1
        num1 = num1 + 0.5
        return round(num1)
    
def problem4(radius,height,pi=3.1415):
    pi = pi
    volume = pi*radius**2*height
    return volume


def problem5(radius,height,pi=3.1415):
    pi = pi
    if type(radius) not in [int,float] or type(height) not in [int,float] or type(pi) not in [int,float] :
        return -1
    volume = pi*radius**2*height
    return volume

def problem6(string):
    sonuc = ""
    for char in string:
        k = char
        flag = 0
        for a in string:
            if a == k:
                flag += 1
        if flag == 1:
            sonuc += k
        else:
            continue       
    return sonuc

def problem7(karakterler):
    for x in range(len(karakterler) - 1):
        if karakterler[x] > karakterler[x + 1]:
            return False
    return True
            
def problem8(string):
    for char in string:
        k = char
        flag = 0
        for a in string:
            if a == k:
                flag += 1
        if flag != 1:
            return False
        else:
            continue       
    return True  