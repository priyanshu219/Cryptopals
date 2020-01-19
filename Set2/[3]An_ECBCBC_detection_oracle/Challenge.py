from random import randint
from Crypto.Cipher import AES

mode='NONE'
block_size = 16

def pad(txt):
	padding_to_add = block_size - len(txt)%block_size
	for i in range(0, padding_to_add):
		txt += bytes([padding_to_add])

	return txt


def Xor(a, b):
	xored=b''
	for i in range(0,len(a)):
		xored += chr(ord(a[i])^ord(b[i]))
	return xored.encode()


def create_random(length):
	txt=''
	for i in range(0, length):
		txt += chr(randint(0, 256))

	print("text:", len(txt))
	print("txt encode : ", len(txt.encode()))

	return txt.encode()

def AES_128_ECB_encrypt(txt, key):
	cipher = AES.new(key, AES.MODE_ECB)
	encrypted = cipher.encrypt(txt)
	return encrypted

def AES_128_CBC_encrypt(txt, key):
	init_vec = create_random(block_size);
	encrypted=b''
	encrypted = AES_128_ECB_encrypt(Xor(txt[0:16], init_vec), key)
	for i in range(16, len(txt), 16):
		encrypted += AES_128_ECB_encrypt(Xor(txt[i:i+16], encrypted[i-16:i]), key)

	return encrypted

def is_ECB(cipher):
	for i in range(0, len(cipher), 16):
		for j in range(i+16, len(cipher), 16):
			if(cipher[i:i+16] == cipher[j:j+16]):
				return True

	return False

def encryption_oracle(txt):
	txt = pad(txt)
	key = create_random(block_size).decode()
	print("Key size : ", len(key))
	print(key)
	cipher=b''
	if(randint(0, 2)):
		cipher = AES_128_ECB_encrypt(txt, key)
		mode='ECB'

	else:
		cipher = AES_128_CBC_encrypt(txt, key)
		mode='CBC'

	print(cipher)
	return cipher

def identify_encryptionmode(cipher):
	if(is_ECB(cipher)):
		return 'ECB'

	else:
		return 'CBC'


def main():
	txt = create_random(50) + b'A'*(randint(4, 56))+ b'A'*(randint(1, 45)) + create_random(78)
	txt = create_random(randint(5, 11)) + txt + create_random(randint(5, 11))
	
	print("-----Original Message----")
	print(txt)
	print()
	print("-----Encrypted Message----")
	encryption = encryption_oracle(txt)
	print()
	if(mode==identify_encryptionmode(encryption)):
		print("Yahoo detected")
	else:
		print("Better luck next time")

if __name__ == '__main__':
	main()