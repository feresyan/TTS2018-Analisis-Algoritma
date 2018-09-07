# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:26:40 2018

@author: feresyan
"""

bilangan = []
kamus = []

def tts2018():
    angka = ''
    bil = input("Masukan 3 buah Bilangan !\n") #input 3 buah bilangan untuk kamus, baris dan kolom
    length = len(bil) #mengambil panjang inputan user
    
    #perulangan untuk memasukan inputan user kedalam list bilangan
    for i in range(0,length):
        if bil[i] != ' ': #jika string yang dibaca bukan spasi, maka masukan nilai string kedalam var angka
            angka += bil[i]
            if (i == length-1): #jika string ke-i merupakan string terakhir, maka masukan nilai ke list bilangan
                angka = int(angka) #mengubah tipe string ke int
                bilangan.append(angka)
                angka = ''
        else: #jika string yang dibaca spasi, maka masukan nilai angka kedalam list bilangan
            angka = int(angka)
            bilangan.append(angka)
            angka = ''
    #Pengecekan terhadap bilangan yang diinputkan user
    if len(bilangan) < 3 :
        print('error : Anda tidak memasukan 3 bilangan!')
    else:
        #Pengecekan nilai kamus, baris dan kolom
        if bilangan[0] < 1 or bilangan[0] > 10 :
            print('error : nilai kamus lebih dari 10 atau kurang dari 1')
        elif bilangan[1] < 1 :
            print('error : nilai baris kurang dari 1')
        elif bilangan[2] < 1 or bilangan[2] > 6 :
            print('error : nilai kolom lebih dari 7 atau kurang dari 1')
        else:
            inputKamus()
        
def inputKamus():
    word = ''
    print('\nMasukan',bilangan[0],'kata sebagai kamus! (Pisahkan dengan spasi antar kata)')
    words = input() #input n buah kata untuk dijadikan kamus
    length = len(words)
    
    for i in range(0,length):
        if words[i] != ' ': #jika string yang dibaca bukan spasi, maka masukan nilai string kedalam var word
            word += words[i]
            if (i == length-1): #jika string ke-i merupakan string terakhir, maka masukan nilai word ke list kamus
                kamus.append(word)
                word = ''
        else: #jika string yang dibaca spasi, maka masukan nilai word kedalam list kamus
            kamus.append(word)
            word = ''
    print(kamus)
    
tts2018()