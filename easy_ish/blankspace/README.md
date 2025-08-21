# Blankspace
## Misc

Can you figure out what this file says?

- Two different types of spaces, either unicode \u0020 or \u2003, this can be seen when opening in a text editor
- Convert different spaces to binary, can be done with a script:
with open("blankspace.txt", "r", encoding="utf-8") as file:
    unicode_message = file.read()
binary_message = ''.join(['0' if char == '\u0020' else '1' for char in unicode_message])
binary_message = ' '.join([binary_message[i:i+8] for i in range(0, len(binary_message), 8)])
print(binary_message)
- convert binary to text

CTF{n0t_4ll_sp4c3s_r_=}