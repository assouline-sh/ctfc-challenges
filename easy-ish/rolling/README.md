#  Rolling Into the New Year
## Misc

New year, same pranks. 

- Run fcrackzip to find password to unzip file: `fcrackzip -D -p rockyou.txt -u rolling.zip`
- Password is zippo123, unzip the file with this password
- Identify the .wav file as morse code, upload to online decoder to find message MORSECODETOTHERESCUE
- Find the file (img725.png) with a different size (142kb)
- Use steghide with the morse code password to find the flag: `steghide extract -sf img725.jpg -p MORSECODETOTHERESCUE`


CTF{3mb3d3d_53cr375}
