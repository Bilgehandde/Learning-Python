# -*- coding: utf-8 -*-
"""
OLCHLT
"""
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem1(List,Index):
    if Index < 0 or Index >= len(List): return None
    return List[Index]

def problem2(List,Index):
    if Index < 0 or Index >= len(List): return List
    new_List = List[:Index] + List[Index + 1:]
    return  new_List 


def problem3(List, ascend):
    
    k = len(List)

    for i in range(k - 1):
        for j in range(0, k-i-1):
            if ascend:
                if List[j] > List[j + 1]:
                    List[j], List[j + 1] = List[j + 1], List[j]
            else:
                if List[j] <List[j + 1]:
                    List[j], List[j + 1] = List[j + 1], List[j]

    return List

def problem4(numbers,weight):
    mult = 0
    sum_weight = 0
    for i in range (0,len(weight)):
        mult += weight[i]*numbers[i]
        
    for i in range (0,len(weight)):
        sum_weight += weight[i] 
    return mult/sum_weight

def problem5(list1, list2):
    flag = 0

    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                flag += 1
                break  

    return flag


def problem6(List):
   
    if not List or not all(len(row) == len(List) for row in List):
        return None

    size = len(List)
    if size == 1:
        return float(List[0][0])

    determinant = 0
    sign = 1
    for col in range(size):
       
        product = 1
        for row in range(size):
            product *= List[(row + col) % size][row]
            # print(product)
        determinant += sign * product
        sign = -sign

    return float(determinant)

def problem7(accounts, source, lira, kurus):

    if source < 0  or source >= len(accounts):
        return accounts
    # Hesaplardaki para ve kuruş miktarlarını ayırır.
    source_money = float(accounts[source])
    source_penny = round(source_money % 1,2)
    source_money = int(source_money)
    # print(source_money)
    # print(source_penny)
    
    kurus = round(kurus/100,2)
    # print(kurus)
    
    withdraw = lira + kurus
    source_sum = round(source_money + source_penny,2)
    
    if source_sum < withdraw :
        return accounts
   
    source_sum = round(source_sum - withdraw,2)
    accounts[source] = f"{source_sum:.2f}"
    
    return accounts

def problem8(num):
    control = 0
    
    for i in range(2, num + 1):
        eliminate = (control + 8) % i
        control = eliminate + 1
    
    return control + 1
 
def problem9(List):
    seen = []
    for i in List:
        if isinstance(i, str):
            if i in seen:
                return i
            seen.append(i)
    return None  