import binascii

buf=input()
buf=binascii.unhexlify(buf)

def find_key(buf):
	f = []
	max_f=0
	key=0

	for i in range(0, 256):
		f.append(0)
		decrypt=''

		for x in buf:
			decrypt+=chr(i^ord(chr(x)))

		for x in decrypt:
			if((ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122)
				or ord(x)==20):
				f[i]+=1

		if(f[i]>max_f):
			key=i

	return key
 


if __name__ == '__main__':
	key = find_key(buf)

	ans=''
	for x in buf:
		ans+=hex(key^ord(chr(x)))[2:]

	print (ans)