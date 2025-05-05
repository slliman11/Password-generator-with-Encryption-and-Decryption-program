# for finding modular inverse
def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None
	else:
		return x % m

# Encryption function
def encrypt(text, key):
	'''
	C = (k*P) % 26
	'''
	return ''.join([ chr((( key*(ord(p) - ord('A'))) % 26)
				+ ord('A')) for p in text.upper().replace(' ', '') ])

# Decryption function
def decrypt(cipher, key):
	'''
	P = (k^-1 * C ) % 26
	'''
	return ''.join([ chr((( modinv(key, 26)*(ord(c) - ord('A'))) % 26)
					 + ord('A')) for c in cipher ])

def main():
	# Menu
	while True:
		number = int(input("Encryption and Decryption program\n\nChoose the number:-\n1. Encrypt \n2. Decrypt \n3. Exit\n="))
		if number == 1:                                         # Encryption
			text = str(input('Enter the text: '))               # insert the text for
			key = int(input('Enter the key: '))                 # insert the key
			encrypted_text = encrypt(text, key)                 # calling encrypt function
			print('Encrypted Text: {}'.format(encrypted_text))  # print the ciphertext

		elif number == 2:                                       # Decryption
			text = str(input('Enter the text: '))               # insert the text
			key = int(input('Enter the key: '))                 # insert the key
			decrypted_text = decrypt(text, key)                 # calling decrypt function
			print('Encrypted Text: {}'.format(decrypted_text))  # print the plaintext

		elif number == 3:                                       # Exit from the program
			print('---------------END---------------')
			break

if __name__ == '__main__':
	main()
