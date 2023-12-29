# -*- coding: utf-8 -*-
"""
OLCHLT
"""
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem1(row, column):
    kontrol = [
        [1]
        #[3,2],
        #[3,5,2]
        #[3,8,7,2]
        ]
    for i in range(1,row+1):
        ilk_satir = [3]
        
        for j in range(1,i+1):
            
            if j == 1 and i == 1 or j==i :
                son_satir = 2
                ilk_satir.append(son_satir)
                kontrol.append(ilk_satir)
                # print(kontrol)
            else :
                ekleme = (kontrol[i-1][j-1]) + (kontrol[i-1][j])
                ilk_satir.append(ekleme)
    # print(kontrol[row-1])
    # print(type(len(kontrol)))
    return kontrol[row-1][column-1]

def problem2(s1,s2):  # Büyük küçük karakter hassasiyeti olacağı belirtilmemiş.(sensitivity == False)
    # s1 = bilgehan  s2= hilal   kontrol = ['i','l'] result = len(control)
    kontrol = []
    for_lenght = min(len(s1),len(s2))
    if len(s1)<len(s2):
        change = s2
        s2 = s1
        s1= change
    for a in range(0,for_lenght):
        if s1[a] == s2[a]:
            kontrol.append(s1[a])
    # print(kontrol)
    # print(type(len(kontrol)))
    return len(kontrol)

def problem3(accounts, source, destination, lira, kurus, fee=False):
    # Her bir indeks bir hesaptır.(["11.23", "10.43", "100.63", "0.10"])/Paranın alınacağı hesap (source)/Paranın yatırılacağı hesap(dest.)
    # İstenilen para transferi lira.kurus / fee komisyon.
    # Hesapları kontrol eder
    if source == destination:
        return accounts

    if source < 0 or destination < 0 or source >= len(accounts) or destination >= len(accounts):
        return accounts

    # Hesaplardaki para ve kuruş miktarlarını ayırır.
    source_money = float(accounts[source])
    source_penny = round(source_money % 1,2)
    source_money = int(source_money)
    # print(source_money)
    # print(source_penny)

    destination_money = float(accounts[destination])
    destination_penny = round(destination_money % 1,2)
    destination_money = int(destination_money)
    # print(destination_money)
    # print(destination_penny)
    kurus = round(kurus/100,2)
    transfer_miktari = lira + kurus
    transfer_ucreti = 0
    # print(kurus)
    # Komisyon ücreti hesaplar.
    if (transfer_miktari) < 10:
         transfer_ucreti = 0.1
     
    else : # 10 tl den büyük transfer için %1'lik ücreti döndürür.(son iki basamağı ile)
        transfer_ucreti += round((lira+kurus)*0.01,2)

    # Ücreti tahsil eder.
    if fee:
        source_money = float(source_money)
        source_money -= transfer_ucreti
        
    source_sum = round(source_money + source_penny,2)
    destination_sum = destination_money + destination_penny
        
    # Hesapta yeterli para var mı kontrol eder.
    if source_sum < transfer_miktari :
        return accounts  
  
    # Transferi yapar.
    source_sum = round(source_sum - transfer_miktari,2)
    destination_sum = round(destination_sum + transfer_miktari,2)

    accounts[source] = f"{source_sum}"
    accounts[destination] = f"{destination_sum}"

    return accounts  