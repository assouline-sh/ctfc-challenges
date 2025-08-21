# Passwords
## Web

I heard passwords are insecure, so my site doesn’t use them!

- Analyze the source code; admin123 needs to be the username entered in the website to navigate to the correct /<uid> path, but there is a check that prevents this
- Bypass this by calculating the UID5 of leet and admin123 and then just navigate to that path by replacing the end of the url with the uid
- `Import uuid`
- `leet=uuid.UUID('13371337-1337-1337-1337-133713371337')`
- `str(uuid.uuid5(leet,'admin123'))`
- The above commands are from the source code. Running this python code will give you the value of the path to navigate to, which is 3c68e6cc-15a7-59d4-823c-e7563bbb326c


CTF{N3W_YEAR_STILL_P4SSW0RDS}
