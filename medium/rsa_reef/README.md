# RSA Reef
## Crypto

Big numbers so it must be secure!

- Write a script for decryption
c = 5140929431661785813136996111772533192371282352009888989933986577900649527212215
p = 3782335750369249076873452958462875461053
q = 9038904185905897571450655864282572131579
e = 65537

n = p * q
et = (p - 1) * (q - 1)
d = pow(e, -1, et)
m = pow(c, d, n)
print(m.to_bytes(100, "big"))


CTF{Und3r_th3_RSEA}
