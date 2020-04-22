#!/usr/bin/python3
#-*-coding:utf-8-*-

author = "www.hasanbaskin.com"
date = "April 2020"

top = """
# =========================================================================|
#		This Script is Created Only for Personel Using
# =========================================================================|"""

undr = """
# =========================================================================|
#		Created By HBN  	Version: 0.2
# =========================================================================|"""

banner =r"""
 _     _                 _ _ _                          
| |__ | |__  _ __       | (_) |__  _ __ __ _ _ __ _   _ 
| '_ \| '_ \| '_ \ _____| | | '_ \| '__/ _` | '__| | | |
| | | | |_) | | | |_____| | | |_) | | | (_| | |  | |_| |
|_| |_|_.__/|_| |_|     |_|_|_.__/|_|  \__,_|_|   \__, |
                                                  |___/ 
"""

import os 
import re
import csv
import os

#Color Codes
green = "\033[32m"
red = "\033[1;31m"
yellow = "\033[93m"
blue = "\033[36m"
default = "\033[0m"


print(top)
print("\t"+banner)
print(undr)

# Add to new book.
# Have a book control.
def new_registry():
	print(blue+"\n\t\t>> Yeni Kayıt Sistemine Hoşgeldiniz <<"+default)
	while True:
		_book_name_ = input(yellow+"\n[?]"+default+"..Kitap Adı: ")
		if book_controller(_book_name_):
			print("\nGirilen kitap daha önce kayıt edilmiş.\n")
			book_show("uniq",_book_name_)
		else:
			print(green+"[+]"+default)
			break
	_novelist_ = input(yellow+"[?]"+default+"..Yazar Adı: ")
	print(green+"[+]"+default)
	_publisher_ = input(yellow+"[?]"+default+"..Yayınevinin Adı: ")
	print(green+"[+]"+default)
	_finish_time_ = input(yellow+"[?]"+default+"..Bitirme Tarihi: ")
	print(green+"[+]"+default)


	with open("database.csv","a+") as registry:

		registry.write("kitap_adi:{},novelist:{},publisher:{},finishtime:{}\n".format(_book_name_,_novelist_,_publisher_,_finish_time_))
		registry.flush()
		print(green+"\nYeni Kayıt İşlemi Başarıyla Tamamlandı.\n"+default)


# Uniq book controller
def book_show(type, book):

	with open("database.csv") as csvfile:
		dataCaptured = csv.reader(csvfile, delimiter='\n',skipinitialspace=True)
		listLines = []

		for data in dataCaptured:
			listLines.append(data)

		if type == "uniq":
						
			for i in range(0,len(listLines)):
				column = listLines[i]
				a,b,c,d = column[0].split(",")
				if book in a:

					tmp, book_name = a.split(":")
					tmp, novelistName = b.split(":")
					tmp, publisherName = c.split(":")
					tmp, finishTime = d.split(":")
					print(red+"\nKitap Bilgileri\n" +yellow+ "-"*23+default)
					print("Kitap Adı: " + book_name)
					print("Yazarı: " + novelistName)
					print("Yayınevi: " + publisherName)
					print("Bitirme Tarihi: " + finishTime)
					print("-"*25)
					pass
				

		if type == "all":
			sayac = 0
			print(blue+"\n\n Tüm Kitapların Detaylı Listesi\n"+"-"*32+default)
			for i in range(0,len(listLines)):
				column = listLines[i]
				a,b,c,d = column[0].split(",")
				sayac+=1
				tmp, book_name = a.split(":")
				tmp, novelistName = b.split(":")
				tmp, publisherName = c.split(":")
				tmp, finishTime = d.split(":")
				print("\n"+ red + book_name +default+ " Kitabına Ait Bilgiler\n" + yellow + "-"*27 + default)
#				print("Kitap Adı: " + book_name)
				print("Yazarı: " + novelistName)
				print("Yayınevi: " + publisherName)
				print("Bitirme Tarihi: " + finishTime)
				print("-"*25)
			
			print(green+"\n[+].."+default+"Toplam " + yellow + str(sayac) + default + " adet kitap bulundu.\n")
	


		if type == "list":
			sayac = 0
			print(blue+"\n\n Tüm Kitapların Listesi\n"+"-"*25+default)
			for i in range(0,len(listLines)):
				column = listLines[i]
				a,b,c,d = column[0].split(",")
				tmp, book_name = a.split(":")
				sayac+=1
				print(yellow+str(sayac)+") " + default + book_name)

			print(green+"\n[+].."+default+"Toplam " + yellow + str(sayac) + default + " adet kitap bulundu.\n")

#Check before adding books.(Yes/No) 
def book_controller(book_name):

	with open("database.csv") as csvfile:

		dataCaptured = csv.reader(csvfile, delimiter='\n', skipinitialspace=True)
		listLines = []

		for line in dataCaptured:
			listLines.append(line)			


		for i in range (0,len(listLines)):
			column = listLines[i]
			a,b,c,d = column[0].split(",")
			tmp,kitap_adi = a.split(":")
			if book_name == kitap_adi:
				return True		
				


def main():
	
	print(blue + "\n\t >> Lütfen Menüden Yapmak İstediğiniz İşlemi Seçiniz <<" + default)
	print(yellow+"\n[1]"+default+"..Yeni Kitap Ekle")
	print(yellow+"[2]"+default+"..Kitap Sorgula")
	print(yellow+"[3]"+default+"..Tüm Kitapları Göster [Detaylı]")
	print(yellow+"[4]"+default+"..Tüm Kitapları Göster [Liste]")

	islem = input(red + "\n[?]" + default + "..Seçenek Numarası : ")

	if islem == "1":
		new_registry()

	elif islem == "2":
		bookName = input(yellow + "\n[?]" + default + "..Aramak İstediğiniz Kitabın Adını Giriniz : ")
		if book_controller(bookName):
			print(green + "\n[+] " + default + "Kitap Bulundu.\n")
			book_show("uniq",bookName)
		else:
			print(red + "\n\tAradığınız Kitap Bulunamadı.\n" + default)

	elif islem == "3":
		book_show("all","NULL")

	elif islem == "4":
		book_show("list","NULL")

	else:
		print(red+"\n\t!!Hatalı Giriş Yaptınız !!\n"+default)


#start the program and loop

erlik = True
while (erlik == True):
	main()
	_reply_ = input(yellow+"\n\t[?]"+default+"..Yeni İşlem Yapmak İstiyormusunuz ? [E/H]  ")
	if (_reply_ == 'e') | (_reply_ == 'E'):
		os.system("clear")
		erlik = True
		print("\n")
	elif (_reply_ == 'h') | (_reply_ == 'H'):
		erlik = False
		print(green+"\n\t[+]"+default+"...Program Başarıyla Sonlandırıldı..."+green+"[+]\n"+default)
		print(yellow+"\n\t\t[>>]"+default+"...Created By HBN..."+yellow+"[<<]\n"+default)

	else:
		print(red+"\n\n\tHatalı Giriş Yaptınız, Program Sonlandırıldı.\n"+default)
		print(yellow+"\n\t\t[>>]"+default+"...Created By HBN..."+yellow+"[<<]\n"+default)
		erlik = False