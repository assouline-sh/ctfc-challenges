# Snack Time
## Forensics

You've been working hard.. have a nice tall glass of milk to warm up. Treking through these chilly challenges can be difficult, so I'll give you a hint. The first passphrase is 'secret'. That's all you get though! 
Be on your way and good luck!

- `steghide extract -sf milk.jpg` with given password ‘secret’
- Unzip directory, go into tmp directory
- Decrypt whoami.txt with base64, then decrypt caesar box cipher
- Solve the riddle, which is ‘frosty the snowman’
- `steghide extract -sf pillsbury.jpg` with password ‘frosty’
- find flag in flag.txt

CTF{m1lk_n_c00kies}
