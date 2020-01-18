import binascii



def calculate_key(cipher):
	f = []
	max_f=0
	key=0

	for i in range(0, 256):
		f.append(0)
		decrypt=''

		for x in cipher:
			decrypt+=chr(i^ord(x))

		for x in decrypt:
			if((ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122)
				or ord(x)==20):
				f[i]+=1

		if(f[i]>max_f):
			max_f=f[i]
			key=i

	return key


def main():

	cur_max = 0
	overall_max = 0
	ans = ''

	file = open('4.txt', 'r')
	lines = file.readlines()
	for buf in lines:
		buf = buf.strip('\n')
		buf = binascii.unhexlify(buf)
		key = calculate_key(buf)
		decrypt=''

		for i in buf:
			decrypt+=chr(key^ord(chr(i)))
		cur_max = 0
		for i in decrypt:
			if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)
				or ord(i)==20):
				cur_max+=1

		
		if(cur_max > overall_max):
			overall_max = cur_max
			# ans = decrypt
			ans=''
			for x in decrypt:
				ans+=hex(key^ord(x))[2:]

	print(ans)
			

if __name__ == '__main__':
	main()