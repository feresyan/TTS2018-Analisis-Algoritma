# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:26:40 2018

@author: feresyan
"""
#Variabel Global
import numpy as np

bilangan = []
kamus = []
abjad = []
matriks = []
found = False
result = []

def inputBilangan():
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
            boolean = inputKamus()
            return boolean
        
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
    if len(kamus) < bilangan[0]:
        print('error : kamus kurang dari',bilangan[0])
    else:
        hasil = inputAlphabet()
        return hasil
    
def inputAlphabet():
    total_huruf = bilangan[1] * bilangan[2]
    print('\nMasukan',total_huruf,'huruf untuk membentuk tts berukuran',bilangan[1],'x',bilangan[2],'! (Pisahkan dengan spasi antar huruf)')
    huruf = input()
    length = len(huruf)
    
    for i in range(0,length):
        if huruf[i] != ' ':
            abjad.append(huruf[i])
    if len(abjad) < total_huruf:
        print('error : huruf kurang dari',total_huruf)
    else:
        return True


def buatMatriks():
    z = 0
    found = False
    if inputBilangan() == True:
        for x in range(0,bilangan[1]):
            matriks.append([]) #Buat baris matriks
        for x in range(0,bilangan[1]):
            for y in range(0,bilangan[2]):
                matriks[x].append(y)
                matriks[x][y] = abjad[z]
                z +=1
                
    mat = np.pad(matriks,1,'constant')
    
    for word in kamus :
        ix = np.where(np.isin(mat,word[0]))
        for i in range(np.shape(ix)[1]):
            A = np.array(mat)
            wix = 1
            while wix < len(word):
                B = np.array(A[ix[0][0]-1:ix[0][0]+2,ix[1][0]-1:ix[1][0]+2])
                C = np.zeros(np.shape(A),dtype='str')
                print(C)
                print('----------------------')
                C[ix[0][0]-1:ix[0][0]+2,ix[1][0]-1:ix[1][0]+2] = B
                print(C)
                print('xxxxxxxxxxxxxxxxxxxxxx')
                B[1,1] = ''
                if(np.sum(np.isin(B,word[wix]))==0) :
                    found = False
                    break
                ix = np.where(np.isin(C,word[wix]))
                wix+=1
            ix = np.where(np.isin(A,word[0]))
            if wix == len(word) :
                found = True
                break
        if found :
            result.append(word+' ')
            
    if len(result) == 0:
        result.append('-')
        print(result[0])
    else:
        for i in range(0,len(result)):
            print(result[i],end='')          
                
buatMatriks()