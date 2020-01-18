import binascii


def padding(txt, block_size):
	padding_to_add = block_size - len(txt)%block_size

	for i in range(0, padding_to_add):
		txt+=bytes([padding_to_add])

	return txt


def main():
	txt = b"YELLOW SUBMARINE"
	txt = padding(txt, 20)
	print(txt)


if __name__ == '__main__':
	main()