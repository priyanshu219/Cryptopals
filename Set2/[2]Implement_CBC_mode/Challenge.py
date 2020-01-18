import base64
import binascii
from Crypto.Cipher import AES

def unpad(cipher):
	pad_len = ord(cipher[-1])
	return (cipher[:-pad_len])

def XOR(a, b):
	xored=''
	for i in range(0, len(a)):
		xored += chr(ord(chr(a[i]))^ord(chr(b[i])))
	return xored

def AES_ECB_DEC(word, key):
	decipher = AES.new(key, AES.MODE_ECB)
	decoded = decipher.decrypt(word)
	return decoded

def AES_CBC_DEC(cipher, key, init_vec):
	decrypted=''
	for i in range(len(cipher), 16, -16):
		decrypted = XOR(AES_ECB_DEC(cipher[i-16:i], key), 
			cipher[i-32:i-16]) + decrypted
	decrypted = XOR(AES_ECB_DEC(cipher[0:16], key), init_vec) + decrypted
	return unpad(decrypted)


def main():
	file = open('8.txt', 'r')
	lines = file.readlines()
	cipher=''
	for buf in lines:
		cipher += buf.replace('\n', '')

	cipher = base64.b64decode(cipher)
	init_vec = b'\x00'*16
	key = b'YELLOW SUBMARINE'
	decrypted_cipher = AES_CBC_DEC(cipher, key, init_vec)
	print("----Decoded Message---")
	print(decrypted_cipher)


if __name__ == '__main__':
	main()