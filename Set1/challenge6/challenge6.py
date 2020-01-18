import binascii
import base64

def find_key(cipher):
	f=[]
	max_f=0
	key=0
		
	for i in range(0,256):
		f.append(0)
		decrypted=''

		for c in cipher:
			decrypted+=chr(i^ord(c))

		for c in decrypted:
			if ((ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122) or ord(c)==32):
				f[i]+=1
			if(f[i] > max_f):
				max_f = f[i]
				key = i
	return key

def edit_distance(a, b):
	t=''
	for i in range(0, len(a)):
		t+=bin(ord(a[i])^ord(b[i]))

	cnt=0
	for i in range(0, len(t)):
		if(t[i] == '1'):
			cnt+=1
	return cnt

def normalization(txt, l):
	value = 0
	cnt = 0
	for i in range(0, len(txt), 2*l):
		if(i+2*l <= len(txt)):
			value+=edit_distance(txt[i:i+l], txt[i+l:i+2*l])
			cnt+=1

	normalize_value = 1.0*value/(l*cnt)

	return normalize_value

def multi_byte_xor(cipher, key):
	decrypt = ''
	for i in range(0, len(cipher)):
		decrypt+=chr(ord(key[i%len(key)])^ord(cipher[i]))

	print(decrypt)



def main():
	file = open('6.txt', 'r')
	lines = file.readlines()
	txt=''
	key_len=0
	min_edit_dis=100000000000
	edit_dis=0
	key=''

	for buf in lines:
		txt+=buf.strip('\n')

	txt=base64.b64decode(txt).decode()

	for i in range(2, 41):
		edit_dis = normalization(txt, i)
		if(min_edit_dis > edit_dis):
			min_edit_dis = edit_dis
			key_len = i

	print ("keylength : ",key_len)
	
	for i in range(0, key_len):
		_txt=''
		for j in range(i, len(txt), key_len):
			_txt+=txt[j]
		key+=chr(find_key(_txt))	

	print("key: ", key)
	print()
	print("--Decoded Text---")
	multi_byte_xor(txt, key)

if __name__ == '__main__':
	main()