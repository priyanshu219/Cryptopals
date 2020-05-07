import base64
from Crypto.Cipher import AES
import  encryption
from random import randint

global key, block_length, encrypted_msg

def random_data(length):
	data=b''
	for i in range(length):
		data += bytes([randint(0,255)])

	return data

def oracle(txt):
	return encryption.AES_128_ECB_encrypt(txt)

def calculate_block_length(cipher):
	inp=b'A'
	initial_len=len(oracle(inp+cipher))
	while True:
		inp+=b'A'
		length = len(oracle(inp+cipher))
		if(length > initial_len):
			return (length - initial_len)

def find_mode(block_length):
	test = random_data(25) + b'A'*randint(1,10)*block_length + b'A'*randint(2,10)*block_length
	cipher = oracle(test)
	if is_ECB(cipher):
		return "ECB_MODE"
	else:
		return "CBC_MODE"

def is_ECB(cipher):
	block_length = calculate_block_length(encrypted_msg)
	for i in range(0,len(cipher)-block_length):
		for j in range(i+1, len(cipher)-block_length+1):
			if(cipher[i:i+block_length] == cipher[j:j+block_length]):
				return True
	return False

def next_chr(known_string, block_length):
	block_len = (block_length - 1 - len(known_string))%block_length
	block = b'A'*block_len
	guess = block + known_string
	for i in range(256):
		l = len(guess)
		if(oracle(block+unknown_string)[:l+1] == oracle(guess+bytes([i]))[:l+1]):
			return bytes([i])

def decryption():
	print('Decryption')
	block_length = calculate_block_length(encrypted_msg)
	if 'ECB' in find_mode(block_length):
		print('ECB mode detected\n\n')
		msg = b''
		for i in range(len(unknown_string)):
			msg += next_chr(msg, block_length)
		print(msg.decode())

if __name__ == '__main__':
	unknown_string = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
	encrypted_msg = oracle(unknown_string)
	decryption()