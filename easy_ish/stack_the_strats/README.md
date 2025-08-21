# Stack the Strats
## Misc

This challenge is a little bit of forensics, a little bit of crypto, a little bit of something else..?


- Run exiftool on the image, see it has trailing data. In hex editor, you can see additional hex data after the PNG footer. And it looks like XGU{... Looks like a substitution ciphertext
- Use quipquip to brute force ciphertext since we know XGU=CTF. Get the result: CTF{this is a fake flag, must face off in cup stack to get the real one}
- Must face off in cup stack. If they win, give paper with /PCZmJy7a on it
- Original image hints to go to pastebin; go to https://pastebin.com/PCZmJy7a and see the flag


CTF{paste_it_again!}

