#ChinuLz Ganteng ChinuLz Ganteng ChinuLz Ganteng ChinuLz Ganteng ChinuLz Ganteng
# [Maaf Masih Berantakan Codingannya😅]
# Kalo Mau Recode Nama Author Jangan Dihapus Ya😘
# Hargai Nama Author

from prettytable import PrettyTable
from gtts import gTTS
from jimner import jimner
import os
import sys
import time
import random

# warna
hijau = '\x1b[1;92m'
kuning = '\x1b[1;93m'
merah = '\x1b[1;91m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'

def Nulz():
	print(ungu + "\nTunggu 3 Detik...")
	time.sleep(2)
	print("3")
	time.sleep(1)
	print("2")
	time.sleep(0.50)
	print("1")
	os.system("clear")
	print("%s"%(merah))
	
	tbl = PrettyTable()
	tbl.field_names = ["Information", "Links"]
	tbl.add_row(["%sAuthor"%(kuning) + ungu, "NuLz404" + merah])
	tbl.add_row(["%sGithub"%(kuning) + ungu, "https://github.com/nulz404" + merah])
	tbl.add_row(["%sEmail"%(kuning) + ungu, "nulz404@proton.me" + merah])
	tbl.add_row(["%sTelegram"%(kuning) + ungu, "https://t.me/nulz404" + merah])
	print(tbl)
	
	art = jimner()
	print(putih)
	art.get_banner_from_text("Sub-Zero", "Magick")
	art.get_banner_from_text("Sub-Zero", "Voice")
	print(merah)
	art.get_banner_from_text("Shadow", "NuLz404")
	
	load = "%sLoading..."%(biru)
	for i in load:
		time.sleep(0.2)
		sys.stdout.write(i)
		sys.stdout.flush()
		
	time.sleep(2)
	textnya = input("%s\n\nMasukan Kata : "%(kuning))
	pro = "%s\nProcessing..."%(biru)
	for i in pro:
		time.sleep(0.2)
		sys.stdout.write(i)
		sys.stdout.flush()
	
	bahasa = "id"
	output = gTTS(text = textnya, lang = bahasa)
	#ran = ('-', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-')
	#dom = ('-', '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '-')
	#num = ('-', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', '-')
	#rran = random.choice(ran)
	#rran2 = random.choice(ran)
	#rrdom = random.choice(dom)
	#rrnum = random.choice(num)
	dt = time.localtime()
	current_time = time.strftime("%H-%M-%S", dt)
	file = 'Audio-Jam-' + current_time
	namafile = file + '.mp3'
	output.save(namafile)
	os.system("mv " + namafile + " SavedAudio")
	time.sleep(0.5)
	tbl2 = PrettyTable()
	print(hijau)
	tbl2.field_names = ['Succes', 'Saved']
	tbl2.add_row(['%sNama File'%(kuning) + ungu, namafile + hijau])
	print(tbl2)
	time.sleep(0.5)
	play = "%s\nMemutar Audio...\n"%(biru)
	for i in play:
		time.sleep(0.2)
		sys.stdout.write(i)
		sys.stdout.flush()
	os.system("mpv SavedAudio/" + file + ".mp3")
	print("====================\n")
	print("\nPilih Opsi Dibawah\n")
	print("1. Buat Lagi")
	print("2. Keluar")
	print("3. Putar Audio")
	print("4. Chat Author")
	pilihan = input("Pilih : ")
	if pilihan == "1" or pilihan == "Buat Lagi":
		Nulz()
	elif pilihan == "2" or pilihan == "Keluar":
		yakin = input("Yakin Keluar? (y/n) ")
		if yakin == "y" or yakin == "Y":
			print("Anda Keluar!")
			exit()
		elif yakin == "n" or yakin == "N":
			Nulz()
		else:
			print("Hmzz Gaje")
	elif pilihan == "3" or pilihan == "Putar Audio":
		print("====================")
		print("list audio saved")
		os.system("ls SavedAudio")
		print("====================")
		aud = input("Pilih : ")
		if aud == aud:
			os.system("mpv SavedAudio/" + aud)
		else:
			print("Pilihan Tidak Valid")
	elif pilihan == "4" or pilihan == "chat":
		os.system("xdg-open https://t.me/nulz404")
	else:
		print("Pilihan Tidak Valid")
pass
Nulz()
#ChinuLz Ganteng ChinuLz Ganteng ChinuLz Ganteng ChinuLz Ganteng ChinuLz Ganteng