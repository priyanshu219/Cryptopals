from Crypto.Cipher import AES
import base64
from random import randint


def random_key(length):
	key=b''
	for i in range(length):
		key += bytes([randint(0,255)])
	return key

def pkcs7_pad(string, block_length):
	length = len(string)
	if(length%block_length == 0):
		return (string+bytes([block_length])*block_length)
	else:
		add = block_length - length%block_length
		
		return(string+bytes([add])*add)

def pkcs7_unpad(string):
	last=string[-1]
	return(string[:-1*last])

key = random_key(16)

def AES_128_ECB_encrypt(string,key):
	string = pkcs7_pad(string, len(key))
	encrypted_key = AES.new(key, AES.MODE_ECB)
	return encrypted_key.encrypt(string)

def AES_128_ECB_decrypt(string,key):
	decryted_key=AES.new(key,AES.MODE_ECB)
	padded_string = decryted_key.decrypt(string)
	return pkcs7_unpad(padded_string)