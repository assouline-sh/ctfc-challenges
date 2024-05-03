# Trick Xor Treat
## Crypto

- Convert hex string to byte array since cryptographic operations, especially bitwise operations like XOR, work with raw binary data
- Iterate through possible values for the single byte the data was XORed with
- in binary, a byte can have 8 bits and each bit is either 0 or 1. so, there are 2^8 or 256 possible combinations of 8 bits, ranging from 0 to 255. 
- for each byte in the ciphertext, it performs a bitwise XOR operation with current potential XOR key, then it is converted back to a character, and the values are concatenated
- if the string has CTF{ in it, we have found the flag

sample solution:
#!/usr/bin/env python3

ciphertext = bytearray.fromhex("5344566b206821204f79634f7d694f7624664f7e657d7223626d")

flag = ""
for num in range(256):
	results = [chr(n^num) for n in ciphertext]
	flag = "".join(results)
	if flag.startswith("CTF{"):
		print(flag)
		print(num)
		
CTF{0x10_is_my_f4v_numb3r}