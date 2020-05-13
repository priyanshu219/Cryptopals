import base64
from Crypto.Cipher import AES
import  encryption
from random import randint
import os

global key, block_length, encrypted_msg
randon_text=os.urandom(randint(1,255))

def random_data(length):
	data=b''
	for i in range(length):
		data += bytes([randint(0,255)])

	return data

def encryption_oracle(txt):
	txt = txt + randon_text
	return encryption.AES_128_ECB_encrypt(txt)

def new_oracle(oracle, block_length):
	def simpler_oracle(text):
		extra = b'a'*(3*block_length)
		new_text = extra+text
		cipher=oracle(new_text)
		for i in range(len(cipher)):
			if(cipher[i:i+16]==cipher[i+16:i+32]==cipher[i+32:i+48]):
				return cipher[i+48:]

	return simpler_oracle

def calculate_block_length():
	inp=b''
	initial_len=len(encryption_oracle(b''))
	while True:
		inp+=b'A'
		length = len(encryption_oracle(inp))
		if(length > initial_len):
			return (length - initial_len)

def find_mode(oracle, block_length):
	test = random_data(25) + b'A'*randint(1,10)*block_length + b'A'*randint(2,10)*block_length
	cipher = oracle(test)
	if is_ECB(cipher):
		return "ECB_MODE"
	else:
		return "CBC_MODE"

def is_ECB(cipher):
	block_length = calculate_block_length()
	for i in range(0,len(cipher)-block_length):
		for j in range(i+1, len(cipher)-block_length+1):
			if(cipher[i:i+block_length] == cipher[j:j+block_length]):
				return True
	return False


def next_chr(oracle, known_string, block_length):
	block_len = (block_length - 1 - len(known_string))%block_length
	block = b'A'*block_len
	guess = block + known_string
	for i in range(256):
		l = len(guess)
		if(oracle(block+unknown_string)[:l+1] == oracle(guess+bytes([i]))[:l+1]):
			return bytes([i])

def decryption(oracle):

	print('Decryption')
	block_length = calculate_block_length()
	oracle = new_oracle(oracle, block_length)
	print('Key Length -> ',block_length)

	if 'ECB' in find_mode(oracle,block_length):
		print('ECB mode detected\n\n')
		msg = b''
		for i in range(len(unknown_string)):
			msg += next_chr(oracle, msg, block_length)
		print(msg.decode())

	else:
		print('Mode not detected')

if __name__ == '__main__':
	unknown_string = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
	decryption(encryption_oracle)