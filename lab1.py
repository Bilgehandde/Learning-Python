# -*- coding: utf-8 -*-
"""
OLCHLT
"""

my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem1():
    name = f"{my_name}"
    return name[0]

def problem2():
    num = int(input("Enter a number: "))
    num = num%8
    ch = my_name[num]
    return ch

def problem3():
    frst = int(input("Enter first number: "))
    scnd = int(input("Enter second number: "))
    frst = frst%8
    scnd = scnd%8
    ch = my_name[min(frst,scnd):max(frst,scnd+1)]
    return ch

def problem4():
    inp = str(input ("Enter input: "))
    harfler = "A a E e U u i I O o"
    sayac = 0 
    if 1 <= len(inp) <= 100:
        for char in harfler:
            if char in inp:   
                sayac += 1
        return sayac 
    
def problem5():   
    k=0
    toplam=0
    while k < 12:
        toplam += int(my_id[k])
        k+=1   
    return toplam

def problem6():
    number = int(input("Enter input: "))
    factorial = 1
    if 1 <= number <= 30:
        for k in range(1, number+1):
            factorial *= k
        return factorial
    elif number > 30 :
        print("Input must be equal or small 30! ")
    elif number == 0 :
        return factorial
    
def problem7():
    sayi = int(input("Enter a number: "))   
    if sayi%3 == 0 and sayi%7 == 0:
        return True
    else: 
        return False
 
def problem8():
    İnput = int(input("Enter a number: "))
    if İnput%3 == 0 and İnput%7 == 0:
        return 3
    elif İnput%3 != 0 and İnput%7 == 0:
        return 2
    elif İnput%3 == 0 and İnput%7 != 0:
        return 1
    
# def problem9():
#     k = 1
#     primecheck = int(input("Enter a number: "))
#     for _ in range(99):
#         if (primecheck % k) != 0:
#             k += 1
#             return False
#     else : 
#         return True
                     
def problem10():
    root = float(input("Enter a number: "))     
    yineleme = 1000
    epsilon=1e-9
    tahmin = root/2
    if 1E9 >= root >= 0.0 :
        for _ in range(yineleme):
            yenithmn = (tahmin + root/tahmin) / 2
            if  abs(yenithmn-tahmin) < epsilon:
                return float(yenithmn)
            tahmin = yenithmn
        return tahmin            

if __name__ == "__main__":
        
     print("Running problem 1")
     print( problem1() )
    
     print("\nRunning problem 2")
     print( problem2() )
    
     print("\nRunning problem 3")
     print( problem3() )
    
     print("\nRunning problem 4")
     print( problem4() )
    
     print("\nRunning problem 5")
     print( problem5() )
    
     print("\nRunning problem 6")
     print( problem6() )
    
     print("\nRunning problem 7")
     print( problem7() )
     
     print("\nRunning problem 8")
     print( problem8() )
    
     print("\nRunning problem 9")
     print( problem9() )
    
     print("\nRunning problem 10")
     print( problem10() )