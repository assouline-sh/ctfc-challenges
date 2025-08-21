# Xor Exposed
## Crypto

Ugh, I always mess up encryption and you’ve always been able to find my flag in the past! But the secrets module is secure, so you won’t be able to guess my key!


- Because it is XOR encryption, the encryption and decryption key are the same. When you have plaintext P and ciphertext C, you can find the key with P XOR C. We notice the key is 4 bytes long and we know 4 bytes of the plaintext (since the plaintext starts with ctf{) so we can write a solve script:
```
def xor(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])
encrypted_flag = "c9d50afbd2911edfc3db33f299d75ff2d9900eec99fe1bb19dc933ebc4911beef5d15db49bcf5bb3d29611"
flag_fragment = b"ctf{"
flag_in_bytes = bytes.fromhex(encrypted_flag)
key = xor(flag_in_bytes, flag_fragment)[:4]
plaintext = xor(flag_in_bytes, key)
print(plaintext)
```

ctf{x0r_iz_r3v3rs1bl3_w17h_kn0wn_p141n73x7}

