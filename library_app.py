#!/usr/bin/python3
#-*-coding:utf-8-*-

author = "HBN"
date = "27.03.2020"

ust = """
# =========================================================================|
#		This Script is Created Only for Personel Using
# =========================================================================|"""

alt = """
# =========================================================================|
#		Created By HBN  	Version: V.1
# =========================================================================|"""


import os 
import re
import csv
import os

#Renk Kodları
yesil = "\033[32m"
red = "\033[1;31m"
sari = "\033[93m"
mavi = "\033[36m"
default = "\033[0m"


print(ust)
os.system("figlet HBN-LIBRARY")
print(alt)

# Yeni kitap eklenmesini sağlayacak.
# Eklenecek olan kitap var mı diye önce kontrol edilecek.

def new_registry():
	print(mavi+"\n\t\t>> Yeni Kayıt Sistemine Hoşgeldiniz <<"+default)
	while True:
		_book_name_ = input(sari+"\n[?]"+default+"..Kitap Adı: ")
		if book_controller(_book_name_):
			print("\nGirilen kitap daha önce kayıt edilmiş.\n")
			book_show("uniq",_book_name_)
		else:
			print(yesil+"[+]"+default)
			break
	_novelist_ = input(sari+"[?]"+default+"..Yazar Adı: ")
	print(yesil+"[+]"+default)
	_publisher_ = input(sari+"[?]"+default+"..Yayınevinin Adı: ")
	print(yesil+"[+]"+default)
	_finish_time_ = input(sari+"[?]"+default+"..Bitirme Tarihi: ")
	print(yesil+"[+]"+default)


	with open("database.csv","a+") as registry:

		registry.write("kitap_adi:{},novelist:{},publisher:{},finishtime:{}\n".format(_book_name_,_novelist_,_publisher_,_finish_time_))
		registry.flush()
		print(yesil+"\nYeni Kayıt İşlemi Başarıyla Tamamlandı.\n"+default)


# Tek kitap sorgulandığında gösterilecek.
# Tüm kitaplar sorgulanırsa tüm kitapları ekrana basacak. 2  bölümden oluşması gerekli.

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
					print(red+"\nKitap Bilgileri\n" +sari+ "-"*23+default)
					print("Kitap Adı: " + book_name)
					print("Yazarı: " + novelistName)
					print("Yayınevi: " + publisherName)
					print("Bitirme Tarihi: " + finishTime)
					print("-"*25)

					pass
				

		if type == "all":
			sayac = 0
			print(mavi+"\n\n Tüm Kitapların Detaylı Listesi\n"+"-"*32+default)
			for i in range(0,len(listLines)):
				column = listLines[i]
				a,b,c,d = column[0].split(",")
				sayac+=1
				tmp, book_name = a.split(":")
				tmp, novelistName = b.split(":")
				tmp, publisherName = c.split(":")
				tmp, finishTime = d.split(":")
				print("\n"+ red + book_name +default+ " Kitabına Ait Bilgiler\n" + sari + "-"*27 + default)
#				print("Kitap Adı: " + book_name)
				print("Yazarı: " + novelistName)
				print("Yayınevi: " + publisherName)
				print("Bitirme Tarihi: " + finishTime)
				print("-"*25)
			
			print(yesil+"\n[+].."+default+"Toplam " + sari + str(sayac) + default + " adet kitap bulundu.\n")
	


		if type == "list":
			sayac = 0
			print(mavi+"\n\n Tüm Kitapların Listesi\n"+"-"*25+default)
			for i in range(0,len(listLines)):
				column = listLines[i]
				a,b,c,d = column[0].split(",")
				tmp, book_name = a.split(":")
				sayac+=1
				print(sari+str(sayac)+") " + default + book_name)

			print(yesil+"\n[+].."+default+"Toplam " + sari + str(sayac) + default + " adet kitap bulundu.\n")

#Kitap eklemeden önce kontrol et.(var/yok)
#Doğrudan kitap sorgulamada kullan --> Kitabın özellikleri çağrılacak book_show()'a gidecek. 
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
	
	print(mavi + "\n\t >> Lütfen Menüden Yapmak İstediğiniz İşlemi Seçiniz <<" + default)
	print(sari+"\n[1]"+default+"..Yeni Kitap Ekle")
	print(sari+"[2]"+default+"..Kitap Sorgula")
	print(sari+"[3]"+default+"..Tüm Kitapları Göster [Detaylı]")
	print(sari+"[4]"+default+"..Tüm Kitapları Göster [Liste]")

	islem = input(red + "\n[?]" + default + "..Seçenek Numarası : ")

	if islem == "1":
		new_registry()

	elif islem == "2":
		bookName = input(sari + "\n[?]" + default + "..Aramak İstediğiniz Kitabın Adını Giriniz : ")
		if book_controller(bookName):
			print(yesil + "\n[+] " + default + "Kitap Bulundu.\n")
			book_show("uniq",bookName)
		else:
			print(red + "\n\tAradığınız Kitap Bulunamadı.\n" + default)

	elif islem == "3":
		book_show("all","NULL")

	elif islem == "4":
		book_show("list","NULL")

	else:
		print(red+"\n\t!!Hatalı Giriş Yaptınız !!\n"+default)


#start the program and return program

erlik = True
while (erlik == True):
	main()
	_reply_ = input(sari+"\n\t[?]"+default+"..Yeni İşlem Yapmak İstiyormusunuz ? [E/H]  ")
	if (_reply_ == 'e') | (_reply_ == 'E'):
		os.system("clear")
		erlik = True
		print("\n")
	elif (_reply_ == 'h') | (_reply_ == 'H'):
		erlik = False
		print(yesil+"\n\t[+]"+default+"...Program Başarıyla Sonlandırıldı..."+yesil+"[+]\n"+default)
		print(sari+"\n\t\t[>>]"+default+"...Created By HBN..."+sari+"[<<]\n"+default)

	else:
		print(red+"\n\n\tHatalı Giriş Yaptınız, Program Sonlandırıldı.\n"+default)
		print(sari+"\n\t\t[>>]"+default+"...Created By HBN..."+sari+"[<<]\n"+default)
		erlik = False


