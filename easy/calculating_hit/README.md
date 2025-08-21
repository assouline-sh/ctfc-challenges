# Calculating Hit
## PWN
I created a new calculator app! I’m still working on it though, and it can only add. I’ve hidden a secret flag if your result equals a special number though! 

- Variables a , b , and sum are all stored as signed integers, so only numbers between –2147483648 and 2147483647 can be represented. If numbers given sum to something greater than 2147483647, the integer will wrap around to negative values
- Inspect code, the special number is -1337
- Enter max 2147483647 and 1337 + 2 = 2147482312 

CTF{c4lc_c0nqu3r0r}
