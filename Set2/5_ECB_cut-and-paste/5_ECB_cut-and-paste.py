from Crypto.Cipher import AES
from random import randint
import os
from encryption import AES_128_ECB_encrypt,AES_128_ECB_decrypt,pkcs7_pad,pkcs7_unpad


key = os.urandom(16)

def authorise(parsed_data):
	if(parsed_data[b'role']==b'admin'):
		print('You are admin')
	else:
		print('You are normal user')

def parse(string):
	key_pair = string.split(b'&')
	parser={}
	for i in key_pair:
		(pair_key,pair_value) = i.split(b'=')
		parser[pair_key]=pair_value
	return parser

def encrypt_cookie(simple_cookie):
	return AES_128_ECB_encrypt(simple_cookie, key)

def decrypt_cookie(cipher):
	string = AES_128_ECB_decrypt(cipher,key)
	authorise(parse(string))

def profile_for(emailid):
	uid = bytes([randint(1,9)])
	role = b'user'
	email = (emailid.decode().replace('&','').replace('=','')).encode()
	simple_cookie= (b'email='+email+b'&uid='+uid+b'&role='+role)
	return encrypt_cookie(simple_cookie)

if __name__ == '__main__':
	profile_for(b'a'*14)
	encrypted_admin = profile_for(b'a'*10+pkcs7_pad(b'admin', 16))[16:32]
	malicious = profile_for(b'a'*14)[:32] + encrypted_admin
	print('Inputing malicious code')
	decrypt_cookie(malicious)
	print('----------YOU ARE HACKED----------')
