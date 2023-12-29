# -*- coding: utf-8 -*-
"""
OLCHLT

"""
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem1():
    yon = str(input("Enter the exit route:"))
    dogu = 0    
    batı = 0
    kuzey = 0
    guney = 0
    for char in yon :
        if char == "n":
            kuzey += 1
        elif char == "e":
             dogu += 1
        elif char == "w":
             batı += 1
        elif char == "s":
             guney += 1
    uzaklık = abs(dogu - batı)**2 + abs(kuzey - guney)**2   
    if uzaklık == 0:
        return round(uzaklık,9)
    else :
        tahmin = uzaklık/2
        for _ in range(10000):
            yenithmn = (tahmin + uzaklık/tahmin) / 2
            if  abs(yenithmn-tahmin) < 1e-9:
                return float(yenithmn)
            tahmin = yenithmn
        return round(tahmin,9)