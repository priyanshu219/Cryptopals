def main():
	a = "\x00"*16
	b = "hellohellohellos"

	for i in range(0, len(a)):
		print(ord(a[i])^ord(b[i]))

if __name__ == '__main__':
	main()