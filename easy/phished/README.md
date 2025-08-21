# Phished
## Misc

You spoof the email for the support team and send a message to the previous email you found. You try to extract some information about the admin username… what is it?

- Follow directions in phishing emails. You will need to extract the key from the encrypted key file and then you will use this key to decrypt the file that contains the username.
- `gpg --output key --decrypt key.gpg`        
- `openssl aes-256-cbc -kfile key -d -in user.txt.enc -out user.txt`
- User.txt contains the flag / username


CTF{ctbadmin}

