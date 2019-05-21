#!/usr/bin/env python
#-*- coding: utf-8 -*-

import base64
import os

menu = 0
print("----------------------------------")
print("BASIC Encode and Decode for base64")
print("       By ARZ3L")
print("----------------------------------")
enter = raw_input("Press ENTER ...")
print("========xxx========")
os.system("clear")

while menu != 2:
	print("========xxx========")
	print("1 - Encrypt\n2 - Decrypt")
	print("========xxx========")
	#SELECT
	select = int(input("-> "))
	print("========xxx========")
	#ENCRYPT
	if select == 1:
		en = raw_input("Encrypt -> ")
		x = base64.b64encode(en)
		print("---------------")
		print x
	#DECRYPT
	elif select == 2:
		de = raw_input("Decrypt -> ")
		y = base64.b64decode(de)
		print("---------------")
		print y