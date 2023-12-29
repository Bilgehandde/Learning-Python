# -*- coding: utf-8 -*-
"""
OLCHLT
"""
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem1():
    # input = { x: x ∈ R and 200.0 ≥ x ≥ -100.0}
    fahrenheit = float(input("Enter Fahrenheit degree: "))
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,9)

def problem2():
    # input = { x: x ∈ R and 100.0 ≥ x ≥ -100.0}
    celsius = float(input("Enter Celsius degree: "))
    fahrenheit = (celsius*9/5) + 32
    return round(fahrenheit,9)

def problem3():
    # input = {x: x ∈ ℕ and 1E6 ≥ x ≥ 1}
    number = int(input("Enter a number: "))
    nth_number = number*(2*number-1)
    return nth_number

def problem4():
    # input = {x: x ∈ ℕ and 1E6 ≥ x ≥ 0}
    number = int(input("Enter a number: ")) 
    n_1st = 1
    n_0th = 2
    if number == 0:
        return 2
    elif number == 1:
        return 1
    elif number > 1 :
        n = n_0th + n_1st
        for _ in range(number-2):
            n += n_1st
            n_1st = n-n_1st
    return int(n)

def problem5():
    reverse = str(input("Enter a string: "))
    k = len(reverse)
    result = ""
    for _ in range(k) :
        result += reverse[k-1]
        k-= 1
    return  result 

def problem6(): # optimize edilecek
    metin = str(input("Enter a string: "))        
    istenmeyen = "!$%&\()*+,-./:;<=>?@[\\]^_`{|}~#"+ "'" + '"'
    yeni_metin = ""
    # metindeki her karakteri kontrol edip istenmeyen karakter değilse boş metne ekler.
    for char in metin:
        if char not in istenmeyen :
            yeni_metin += char
    return yeni_metin    

def problem7(): # optimize edilecek
    number = int(input("Enter input: "))
    if number == 0:
        return "0" 
    liste = []
    while number > 0: #Sayı tabanın rakam sayısına bölünebildiği kadar bölünür. 
    # Bölümden kalanlar sondan başa doğru yazıldığında sayının 10'lu karşılığı bulunmuş olur
        basamak = number % 4  # 22 = 4**0*a+4*b+4**2*c ... 
        liste.insert(0,str(basamak)) # listeye bu basamağı ekler
        number = number // 4 
# sayıyı 4 e bölüp bölümü yeni sayı olarak atar ve 4 ten küçük olana kadar döngü devam eder.
    return  "".join(liste)
    # ya da bu yöntemle terse çevrilebilir.
    # result = []
    # for a in liste:
    #     result.insert(0, a)
    # sonuc = "".join(result)
    # return sonuc
    
            
def problem8(): 
    inp = str(input("Enter input: "))
    kontrol = 0
    for char in inp :
        if char == "(":
            kontrol += 1
        elif char == "{":
            kontrol += 1
        elif char == "[":
            kontrol += 1
        elif char == ")":
             kontrol -= 1
             if kontrol < 0:
                 return False
        elif char == "}":
             kontrol -= 1
             if kontrol < 0:
                 return False
        elif char == "]":
             kontrol -= 1
             if kontrol < 0:
                return False           
    return kontrol == 0 
             
def problem9():
    metin = str(input("Enter a string: "))
    return len(metin.split()[-1])


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