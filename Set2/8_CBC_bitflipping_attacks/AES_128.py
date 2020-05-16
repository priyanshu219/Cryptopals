from Crypto.Cipher import AES
import base64
from random import randint
import os

key = os.urandom(16)


class paddingError(Exception):
	'''Exception for incorrect padding'''

def pkcs7_unpad(string):
	last = string[-1];
	return(string[:-1*last])

def check(string):
	string = string.encode()
	last = string[-1]
	test = string[-1*last:]
	for i in test:
		if(i != last):
			raise paddingError
			return
	else:
		# print("correct padding")
		return(pkcs7_unpad(string))


def pkcs7_pad(string, block_length):
	length = len(string)
	if(length%block_length == 0):
		return (string+bytes([block_length])*block_length)
	else:
		add = block_length - length%block_length
		return(string+bytes([add])*add)

def Xor(string1, string2):
	output = b''
	for i in range(len(string2)):
		output += bytes([string1[i]^string2[i]])

	return output


def AES_ECB_128_encrypt(string, key=key, pad=True):
	if(pad):
		string = pkcs7_pad(string, len(key))
	encrypted_key = AES.new(key, AES.MODE_ECB)
	return encrypted_key.encrypt(string)

def AES_ECB_128_decrypt(cipher, key=key, unpad=True):
	decrypted_key = AES.new(key, AES.MODE_ECB)
	string = decrypted_key.decrypt(cipher)
	if(unpad):
		string = check(string)
	return string

def AES_CBC_128_encrypt(string,key=key,IV=b'\x00'*16):
	string = pkcs7_pad(string, len(key))
	cipher = b''
	cipher += AES_ECB_128_encrypt(Xor(string[:16],IV), key, False)
	for i in range(16,len(string),16):
		cipher += AES_ECB_128_encrypt(Xor(string[i:i+16],cipher[i-16:i]), key, False)

	return cipher

def AES_CBC_128_decrypt(cipher, key=key, IV=b'\x00'*16):
	text = b''
	text = Xor(AES_ECB_128_decrypt(cipher[:16],key, False),IV)
	for i in range(16, len(cipher), 16):
		text += Xor(AES_ECB_128_decrypt(cipher[i:i+16], key, False), cipher[i-16:i])

	return pkcs7_unpad(text)
