from AES_128 import AES_CBC_128_encrypt,Xor,AES_CBC_128_decrypt
import os

key = os.urandom(16)

def encryption_oracle(payload):
	prepend = b'comment1=cooking%20MCs;userdata='
	append = b";comment2=%20like%20a%20pound%20of%20bacon"
	text = prepend + payload + append
	return AES_CBC_128_encrypt(text, key)

def verify_admin(string):
	if b';admin=True;' in string:
		print('Welcome admin')
	else:
		print('Welcome User')

def decrypt(attack):
	string = AES_CBC_128_decrypt(attack, key)
	verify_admin(string)

def crack(oracle, payload):
	payload = payload.replace(';','').replace('=','')
	payload = payload.encode()
	cipher = oracle(payload)
	payload_desired = b';admin=True;AAAA'
	malicious  = cipher[:32] + Xor(Xor(payload_desired, payload[16:]),cipher[32:48])+cipher[48:]

	decrypt(malicious)

if __name__ == '__main__':
	payload_actual='A'*16 + 'XadminXTrueXAAAA'
	crack(encryption_oracle, payload_actual)