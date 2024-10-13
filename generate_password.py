#!/bin/python3


import string
import random
import sys



lower_alph = string.ascii_lowercase
upper_alph = string.ascii_uppercase

num = string.digits

chars = string.punctuation

li = [lower_alph, upper_alph, num, chars]

def generate(length):
	passwd = ""
	for _ in range(length):
		random.shuffle(li)
		random.shuffle(li)
		choosen = random.choice(li)
		passwd += random.choice(list(choosen))
	print(passwd)

if len(sys.argv) < 2:
	print("\033[1;32m[\033[0m!\033[1;32m] \033[1;31mError. Password length not specified.\033[1;34m\n\tpython3 generate.py <password length>\033[0m")
	exit()

n = int(sys.argv[1])

try:
	times = int(sys.argv[2])
	print(f"[*] Printing {times}x random {n} length passwords.")
	for _ in range(times):
		print()
		generate(n)
except IndexError:
	generate(n)
