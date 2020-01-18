import binascii
import base64


def test_ecb(cipher):
	cipher = binascii.unhexlify(cipher)
	cnt = 0
	for i in range(0, len(cipher), 16):
		for j in range(i+16, len(cipher), 16):
			if(cipher[i:i+16] == cipher[j:j+16]):
				cnt+=1

	return cnt




def main():
	file = open('8.txt', 'r')
	lines = file.readlines()
	# print(lines[1])
	txt=''
	max_cnt = 0
	for buf in lines:
		cnt = test_ecb(buf.replace('\n', ''))
		if(cnt > max_cnt):
			max_cnt = cnt
			txt = buf
	# print(binascii.unhexlify(txt.replace('\n', '')))
	print(txt)

if __name__ == '__main__':
	main()