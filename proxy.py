#!/usr/bin/env python
import subprocess, time, os
import platform

def squid_port():
	if platform.platform().find("Ubuntu-16.04") > -1 :
		yol="/etc/squid/squid.conf"
		dosya=open(yol).read()
		dosya_port=dosya.split("\nhttp_port ")[1].split("\n")[0]
		print "Mevcut portunuz:", dosya_port
		port=raw_input("Degisecek port numarasini girin: ")
		c_port=dosya.replace("\nhttp_port "+dosya_port+"\n", "\nhttp_port "+port+"\n")
		open("/etc/squid/squid.conf", "w").write(c_port)
		subprocess.call(["sudo", "service", "squid", "restart"])
		print "Port degisti, squid proxy'i kullanabilirsiniz."
	
	else:
		yol="/etc/squid3/squid.conf"
		dosya=open(yol).read()
		dosya_port=dosya.split("\nhttp_port ")[1].split("\n")[0]
		print "Mevcut portunuz:", dosya_port
		port=raw_input("Degisecek port numarasini girin: ")
		c_port=dosya.replace("\nhttp_port "+dosya_port+"\n", "\nhttp_port "+port+"\n")
		open("/etc/squid3/squid.conf", "w").write(c_port)
		subprocess.call(["sudo", "service", "squid3", "restart"])
		print "Port degisti, squid proxy'i kullanabilirsiniz."
	
def squd_remove():
	if platform.platform().find("Ubuntu-16.04") > -1 :
		soru=raw_input("Squid'i kaldirmak istediginizden emin misiniz? (E/H): ")
		if soru == "E" or soru == "e":
			subprocess.call(["sudo", "apt-get", "purge", "--auto-remove", "squid"])
		else:
			print "Hatali secim yaptiniz."

	else:
		soru=raw_input("Squid'i kaldirmak istediginizden emin misiniz? (E/H): ")
		if soru == "E" or soru == "e":
			subprocess.call(["sudo", "apt-get", "purge", "--auto-remove", "squid3"])
		else:
			print "Hatali secim yaptiniz."

while True:	
	menu = raw_input(	"<<<<<< MENU >>>>>>\n"
						"   1) Squid Proxy\n"
                        "   2) Cikis\n"
						"Cevabiniz: ")

		
	if menu == "1":
		while True:
			menu2 = raw_input(	"<<<<<< SQUID PROXY MENU >>>>>>\n"
								"   1- Squid Port Degistir\n"
								"   2- Squid Proxy'i Kaldir\n"
								"   3- Geri\n"
								"Cevabiniz: ")
			if menu2 == "1":
				squid_port()
			elif menu2 == "2":
				squd_remove()
			elif menu2 == "3":
				break
			else:
				print "Gecersiz secim yaptiniz!"
		

	elif menu == "2":
		break
	else:
		print "Gecersiz secim yaptiniz!"
