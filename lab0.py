# -*- coding: utf-8 -*-
'''
OLCHLT
'''
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem1():
    text = "Hi all, This is Bilgehan Dede!"
    return text


def problem2():
    ad = str(input("Enter some input: "))
    return "Input was " + ad

def problem3():
    st_number = int(input("Enter first number: "))
    nd_number = int(input("Enter second number: "))
    outcome = st_number + nd_number
    return outcome

def problem4():
    
    frst_number = float(input("Enter first number: "))
    scnd_number = float(input("Enter second number: "))
    conc = frst_number - scnd_number
    
    return conc

def problem5():
    
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    sonuc = number1 % number2
    return sonuc

def problem6():
    
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    pi = 3.141592
    volume = pi * radius**2 * height
    
    return volume

def problem7():
    
    side = float(input("Enter one side: "))
    cevre = 4*side
    conclusion = "The perimeter of the square is {} "+ format(cevre)+"."
    return conclusion


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