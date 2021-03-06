#!/usr/bin/env python

import base64
import sys

#RC4 Implementation
def rc4_crypt( data , key ):
	S = range(256)
	j = 0
	out = []
	
	#KSA Phase
	#gererate a random list[255] based on the key
	for i in range(256):
		j = (j + S[i] + ord( key[i % len(key)] )) % 256
		S[i] , S[j] = S[j] , S[i]
	#print S
	
	#PRGA Phase
	for char in data:
		i = j = 0
		i = ( i + 1 ) % 256
		j = ( j + S[i] ) % 256
		S[i] , S[j] = S[j] , S[i]
		out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))
	
	return ''.join(out)

# function that encrypts data with RC4 and decodes it in base64 as default
# for other types of data encoding use a different encode parameter 
# Use None for no encoding
def encrypt( data , key , encode = base64.b64encode ):
	data = rc4_crypt(data , key)
	if encode:
        	data = encode(data)
            
	return data

# function that decrypts data with RC4 and decodes it in base64 as default
# for other types of data encoding use a different decode parameter 
# Use None for no decoding
def decrypt(data , key, decode = base64.b64decode ):
	if decode:
		data = decode(data)
	
	return rc4_crypt(data , key)


def main():
	if len(sys.argv) != 3:
		print (" Usage: <data> <key> ")
		return 1
	
	# turn input data and key to tuple
	data = tuple(sys.argv[1])
	key  = tuple(sys.argv[2]) 

	data = encrypt(data, key)
	print data
	data = decrypt(data, key)
	print data
	
	return 0



if __name__ == '__main__':
	main()
