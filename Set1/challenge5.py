import binascii

def multi_xor(stanza, key):
	length = len(stanza)
	ans=''
	key_len = len(key)
	for i in range(0, length):
		ans+=chr(ord(key[i%key_len])^ord(stanza[i]))

	ans = ans.encode('utf-8')
	ans = ans.hex()
	return ans

stanza="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key="ICE"
ans = ''
ans=multi_xor(stanza,key)
print(ans)	