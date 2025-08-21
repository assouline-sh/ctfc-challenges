# Gym Class
## RE

I want to get into the gym after hours to train some more, but I need to give it the flag to unlock the door!

- Decompile the class file (can use an online one) and figure out that it xors the flag with a 2-byte key "\x42\x24", base64-encodes the result & compares it to a static string. base64-decode the static string and xor it with "\x42\x24" to get the flag. https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'Hex','string':'4224'%7D,'Standard',false)&input=QVhBRVh6WldkaFVzZTNaSUxuc21FRHRa&oeol=VT 

CTF{tr41n_4ll_d4y}

