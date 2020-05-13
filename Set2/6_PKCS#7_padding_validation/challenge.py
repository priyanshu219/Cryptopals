def pkcs7_unpad(string):
	last = string[-1];
	print((string[:-1*last]).decode())

def check(string):
	string = string.encode()
	last = string[-1]
	test = string[-1*last:]
	for i in test:
		if(i != last):
			print('Wrong padding')
			return
	else:
		print("correct padding")
		return(pkcs7_unpad(string))

if __name__ == '__main__':
	string = 'ICE ICE BABY\x04\x03\x04\x04'
	check(string)