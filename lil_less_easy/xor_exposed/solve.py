def xor(message, key):
	return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])

encrypted_flag = "c9d50afbd2911edfc3db33f299d75ff2d9900eec99fe1bb19dc933ebc4911beef5d15db49bcf5bb3d29611"

flag_fragment = b"ctf{"

flag_in_bytes = bytes.fromhex(encrypted_flag)

key = xor(flag_in_bytes, flag_fragment)[:4]

plaintext = xor(flag_in_bytes, key)
print(plaintext)
