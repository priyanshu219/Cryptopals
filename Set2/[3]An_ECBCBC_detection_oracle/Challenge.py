from random import randint


def create_key():
	txt=""
	for i in range(16):
		txt += chr(randint(0, 255))
	txt.encode()
	print(txt)
	return txt

print(create_key())