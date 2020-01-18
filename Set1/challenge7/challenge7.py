import base64
from Crypto.Cipher import AES

def decrypt_cipher(ciphertext, key):
	cipher = AES.new(key, AES.MODE_ECB)
	plaintext = cipher.decrypt(ciphertext)
	return plaintext.decode()

def main():
	file = open('7.txt', 'r')
	lines = file.readlines()
	txt=''
	for buf in lines:
		txt+=buf
	txt = base64.b64decode(txt)
	key = b'YELLOW SUBMARINE'
	txt = decrypt_cipher(txt, key)
	print(txt)


if __name__ == '__main__':
	main()