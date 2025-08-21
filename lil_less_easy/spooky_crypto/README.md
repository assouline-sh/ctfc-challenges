# Spooky Crypto
## Crypto

One of the hex values in file.txt were XOR'd with the number 16. Can you find which one it is and find the flag?

- For each line in file.txt, convert into byte array and xor each byte with the number 16
- Convert into a character and join the string together
- If the string starts with CTF{, print it out

Sample solution:
#!/usr/bin/env python3

with open('file.txt', 'r') as file:
	for line in file:
		ciphertext = bytearray.fromhex(line)

		flag = ""
		results = [chr(n^16) for n in ciphertext]
		flag = "".join(results)
		if flag.startswith("CTF{"):
			print(flag)

CTF{crypto_coding}
